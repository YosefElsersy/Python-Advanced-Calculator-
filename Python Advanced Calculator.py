import tkinter as tk
from math import *

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Casio Advanced Calculator")

        # Create display widget
        self.display = tk.Entry(self.master, width=30, font=('Arial', 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        self.create_button("(", 1, 0)
        self.create_button(")", 1, 1)
        self.create_button("C", 1, 2)
        self.create_button("DEL", 1, 3)

        self.create_button("sin", 2, 0)
        self.create_button("cos", 2, 1)
        self.create_button("tan", 2, 2)
        self.create_button("^", 2, 3)

        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("/", 3, 3)

        self.create_button("4", 4, 0)
        self.create_button("5", 4, 1)
        self.create_button("6", 4, 2)
        self.create_button("*", 4, 3)

        self.create_button("1", 5, 0)
        self.create_button("2", 5, 1)
        self.create_button("3", 5, 2)
        self.create_button("-", 5, 3)

        self.create_button("0", 6, 0)
        self.create_button(".", 6, 1)
        self.create_button("+", 6, 2)
        self.create_button("=", 6, 3)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=7, height=2, font=('Arial', 20),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "DEL":
            self.display.delete(len(self.display.get())-1, tk.END)
        elif text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, text)

        if text == "sin":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, sin(float(self.display.get())))
        elif text == "cos":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, cos(float(self.display.get())))
        elif text == "tan":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, tan(float(self.display.get())))
        elif text == "^":
            self.display.insert(tk.END, "**")

if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
