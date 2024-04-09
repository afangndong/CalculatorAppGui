import tkinter as tk
from tkinter import filedialog
import os

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path)
        file_size_bytes = os.path.getsize(file_path)
        file_size_mb = file_size_bytes / (1024 * 1024)  # Convert bytes to megabytes
        file_info_text.set(f"Name: {file_name}\nSize: {file_size_mb:.2f} MB\nPath: {file_path}")

# Create the main window
root = tk.Tk()
root.title("File Information")
root.geometry("300x250")

# Create a label to display file information
file_info_text = tk.StringVar()
file_info_label = tk.Label(root, textvariable=file_info_text, wraplength=280)
file_info_label.pack(pady=10)

# Create a button to open file dialog
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
