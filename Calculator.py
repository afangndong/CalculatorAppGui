import tkinter as tk
import sqlite3
from addition import add
from substraction import sub
from multiplication import mul
from division import div

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.current_input = ""
        self.result_var = tk.StringVar()

        self.result_label = tk.Label(master, textvariable=self.result_var, font=('Helvetica', 20))
        self.result_label.grid(row=0, column=0, columnspan=4)

        button_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in button_texts:
            tk.Button(master, text=text, width=10, height=4, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col)

        # Create a connection to SQLite database
        self.conn = sqlite3.connect('calculation_history.db')
        self.cursor = self.conn.cursor()

        # Create a table to store calculation history if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS calculations
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            operation TEXT,
                            result REAL)''')
        self.conn.commit()

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.current_input)
                self.result_var.set(result)
                self.current_input = str(result)

                # Save the calculation to the database
                self.cursor.execute("INSERT INTO calculations (operation, result) VALUES (?, ?)", (self.current_input, result))
                self.conn.commit()

            except Exception as e:
                self.result_var.set("Error")
                self.current_input = ""
        elif value == 'C':
            self.current_input = ""
            self.result_var.set("")
        elif value in ['+', '-', '*', '/']:
            self.current_input += value
        else:
            self.current_input += value
            self.result_var.set(self.current_input)

        if value == '=':
            try:
                result = None
                if '+' in self.current_input:
                    numbers = self.current_input.split('+')
                    result = addition.add(float(numbers[0]), float(numbers[1]))
                elif '-' in self.current_input:
                    numbers = self.current_input.split('-')
                    result = subtraction.subtract(float(numbers[0]), float(numbers[1]))
                elif '*' in self.current_input:
                    numbers = self.current_input.split('*')
                    result = multiplication.multiply(float(numbers[0]), float(numbers[1]))
                elif '/' in self.current_input:
                    numbers = self.current_input.split('/')
                    result = division.divide(float(numbers[0]), float(numbers[1]))

                if result is not None:
                    self.result_var.set(result)
                    self.current_input = str(result)
            except Exception as e:
                self.result_var.set("Error")
                self.current_input = ""

    def __del__(self):
        # Close the connection when the Calculator instance is deleted
        self.conn.close()
