from tkinter import *
from pynput.keyboard import Listener, Key
from datetime import datetime
import threading

# --- Interface Tkinter ---
root = Tk()
root.title("Keylogger pédagogique")
root.geometry("500x300")

label = Label(root, text="Aucune touche détectée", font=("Arial", 16))
label.pack(pady=20)

text_box = Text(root, width=60, height=10, font=("Consolas", 12))
text_box.pack(pady=10)

# --- Fonction pour mettre dans le truc de Tkinter ---
def update_display(text):
    time = timestamp()
    label.config(text=text)
    text_box.insert(END, time + text + "\n")
    text_box.see(END)

# --- Listener ---

def timestamp():                           
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def on_press(key):
    try:
        update_display(f"[PRESS] {key.char}")
    except AttributeError:
        update_display(f"[PRESS] {key}")

def on_release(key):
    update_display(f"[RELEASE] {key}")
    if key == Key.esc:
        return False

def start_listener():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

threading.Thread(target=start_listener, daemon=True).start()

root.mainloop()
