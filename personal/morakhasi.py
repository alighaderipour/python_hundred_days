import tkinter as tk
from tkinter import StringVar


class SimpleCalculator:
    def __init__(self, master):
        master.title("محاسبه مرخصي")
        master.geometry("400x300")

        # StringVar instances for the input fields and result field
        self.days = StringVar()
        self.six = StringVar()
        self.seven = StringVar()
        self.eight = StringVar()

        # Creating Entry widgets
        tk.Entry(master, textvariable=self.days, width=22).grid(
            row=0, column=1, padx=10, pady=10
        )
        tk.Entry(master, textvariable=self.six, width=22, state="readonly").grid(
            row=1, column=1, padx=10, pady=10
        )
        tk.Entry(master, textvariable=self.seven, width=22, state="readonly").grid(
            row=2, column=1, padx=10, pady=10
        )
        tk.Entry(master, textvariable=self.eight, width=22, state="readonly").grid(
            row=3, column=1, padx=10, pady=10
        )

        # Creating labels
        tk.Label(master, text="تعداد روز :").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(master, text="موظفي 6:45 :").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(master, text="موظفي 7:10 :").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(master, text="موظفي 8:20 :").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(master, text="تهيه شده توسط علي قادري پور").grid(
            row=7, column=0, padx=0, pady=0
        )

        # Creating the Calculate button
        tk.Button(master, text="محاسبه", command=self.calculate).grid(
            row=6, column=1, pady=10
        )
        master.bind("<Return>", lambda event: self.calculate())
        # Creating the Clear button
        tk.Button(master, text="پاك كردن", command=self.clear).grid(
            row=6, column=3, pady=10
        )

    def calculate(self):
        try:
            # Getting the input numbers
            days_input = int(self.days.get())

            # Calculating the result
            six_min = (days_input * 60 * 6) + (days_input * 45)
            six_hour = int(six_min / 60)
            six_val = f"{six_hour} : {six_min - (six_hour * 60)} "

            seven_min = (days_input * 60 * 7) + (days_input * 20)
            seven_hour = int(seven_min / 60)
            seven_val = f"{seven_hour} : {seven_min - (seven_hour * 60)} "

            eight_min = (days_input * 60 * 8) + (days_input * 10)
            eight_hour = int(eight_min / 60)
            eight_val = f"{eight_hour} : {eight_min - (eight_hour * 60)} "

            # Setting the result to the result field
            self.six.set(six_val)
            self.seven.set(seven_val)
            self.eight.set(eight_val)
        except ValueError:
            # If the input is not a number, show an error message
            self.days.set("numbers only")

    def clear(self):
        # Clear the input and result fields
        self.days.set("")
        self.six.set("")
        self.seven.set("")
        self.eight.set("")


root = tk.Tk()
app = SimpleCalculator(root)
root.mainloop()
