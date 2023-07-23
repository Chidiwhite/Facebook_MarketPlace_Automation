# Importing required modules
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess

# Function to change the color of the welcome_label text
def change_text_color():
    current_color = welcome_label.cget("foreground")
    colors = ['grey', 'black', 'white']
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]
    welcome_label.config(foreground=next_color)
    root.after(500, change_text_color)

# Function to ask user to select CSV files
def upload_files():
    files = filedialog.askopenfilenames(title="Select CSV Files", filetypes=[("CSV Files", "*.csv")])
    return list(files)

# Function to run a Python script with CSV files as arguments
def run_python_file(python_file, csv_files):
    command = ["python", python_file]
    command.extend(csv_files)
    subprocess.Popen(command)

# Creating the main application window
root = tk.Tk()
root.title("FastX FacebookMarketPlace Automation Tool")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the geometry to the screen size
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg='black')

# Load and resize the FastX logo
fx_logo = Image.open("logo.png")
desired_width = 100
desired_height = 100
resized_fx_logo = fx_logo.resize((desired_width, desired_height), Image.LANCZOS)
fx_photo = ImageTk.PhotoImage(resized_fx_logo)

# Display the FastX logo on the application window
image_label2 = tk.Label(root, image=fx_photo)
image_label2.pack(padx=10, pady=10)

# Welcome text for the automation tool
welcome_text = 'Welcome to FastX FacebookMarketplace Automation Tool.'
welcome_label = tk.Label(
    root,
    text=welcome_text,
    foreground='white',
    bg="black",
    font=("Helvetica", 25)
)
welcome_label.pack(pady=(100, 5))

# Description for the automation tool
description = "Say goodbye to manual tasks. \nFastX empowers you to automate your \
Facebook Marketplace activities, saving you time and effort."
description_label = tk.Label(
    root,
    text=description,
    font=("Helvetica", 16),
    bg='black',
    foreground='white')
description_label.pack()

# Label to instruct the user to click the button
l1 = tk.Label(root,
              text='Click Button Below',
              width=30,
              font=('times', 18, 'bold'),
              bg='black',
              foreground='lightgrey'
              )
l1.pack(pady=(20,10))

# Function to be executed when the "Select and Run CSV File(s)" button is clicked
def on_select_and_run():
    # Step 1: Upload and get the list of selected CSV files
    csv_files = upload_files()

    # Step 2: Call the function to run the Python file with the selected CSV files
    if csv_files:
        # Replace "run.py" with the filename of your Python script
        run_python_file("run.py", csv_files)

# Button to select and run CSV files
b1 = tk.Button(root,
               text='Select and Run CSV File(s)',
               width=30,
               relief=tk.RAISED,
               font=("Helvetica", 15),
               command=on_select_and_run
               )
b1.pack()

# Function to change the color of the welcome_label text at regular intervals
change_text_color()

# Start the main event loop
root.mainloop()
