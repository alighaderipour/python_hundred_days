import tkinter as tk
from tkinter import StringVar


class SimpleCalculator:
    def __init__(self, master):
        master.title("Simple Calculator")
        master.geometry("300x200")

        # StringVar instances for the input fields and result field
        self.num1 = StringVar()
        self.num2 = StringVar()
        self.result = StringVar()

        # Creating Entry widgets
        tk.Entry(master, textvariable=self.num1, width=10).grid(
            row=0, column=1, padx=10, pady=10
        )
        tk.Entry(master, textvariable=self.num2, width=10).grid(
            row=1, column=1, padx=10, pady=10
        )
        tk.Entry(master, textvariable=self.result, width=12, state="readonly").grid(
            row=2, column=1, padx=10, pady=10
        )

        # Creating labels
        tk.Label(master, text="Number 1:").grid(row=0, column=0)
        tk.Label(master, text="Number 2:").grid(row=1, column=0)
        tk.Label(master, text="Result:").grid(row=2, column=0)

        # Creating the Calculate button
        tk.Button(master, text="Calculate", command=self.calculate).grid(
            row=3, column=1, pady=10
        )

        # Creating the Clear button
        tk.Button(master, text="Clear", command=self.clear).grid(
            row=3, column=0, pady=10
        )

    def calculate(self):
        try:
            # Getting the input numbers
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())

            # Calculating the result
            result = num1 + num2

            # Setting the result to the result field
            self.result.set(result)
        except ValueError:
            # If the input is not a number, show an error message
            self.result.set("numbers only")

    def clear(self):
        # Clear the input and result fields
        self.num1.set("")
        self.num2.set("")
        self.result.set("")


root = tk.Tk()
app = SimpleCalculator(root)
root.mainloop()
