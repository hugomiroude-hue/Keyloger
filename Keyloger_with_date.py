from pynput.keyboard import Listener, Key        
from datetime import datetime                 

def timestamp():                           
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def on_press(key):                            
    time = timestamp()                           
    try:
        print(f"{time} [PRESS] {key.char}")     
    except AttributeError:
        print(f"{time} [PRESS] {key}")       

def on_release(key):                    
    time = timestamp()
    print(f"{time} [RELEASE] {key}")

    if key == Key.esc:
        return False

with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()