# history.py

import tkinter as tk
import sqlite3

def show_history():
    # Create a new window to display history
    history_window = tk.Toplevel()
    history_window.title("Calculation History")

    # Create a connection to SQLite database
    conn = sqlite3.connect('calculation_history.db')
    cursor = conn.cursor()

    # Fetch calculation history from the database
    cursor.execute("SELECT * FROM calculations")
    history = cursor.fetchall()

    # Display history in a text widget
    history_text = tk.Text(history_window)
    for row in history:
        history_text.insert(tk.END, f"{row[1]} = {row[2]}\n")
    history_text.pack()

    # Close the connection
    conn.close()
