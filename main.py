#Main module

#import each module
import tkinter as tk
from Calculator import Calculator




def main():
    root = tk.Tk()
    app = Calculator(root)  # Create an instance of the Calculator class, which will implicitly call its __init__ method
    root.mainloop()

if __name__ == "__main__":
    main()

