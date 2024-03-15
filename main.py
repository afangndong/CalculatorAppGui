#Main module

#import each module
import tkinter as tk
import Calculator




def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
