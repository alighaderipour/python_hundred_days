from tkinter import Tk, Entry, Button, StringVar


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="gray")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""
        Entry(
            width=17, bg="#fff", font=("Arial Bold", 28), textvariable=self.equation
        ).place(x=0, y=0)

        def show(value):
            self.entry_value += str(value)
            self.equation.set(self.entry_value)

        def clear():
            self.entry_value = ""
            self.equation.set(self.entry_value)

        def solve():
            try:
                result = eval(self.entry_value)
                self.equation.set(result)
                self.entry_value = str(result)
            except Exception as e:
                self.equation.set("Error")
                self.entry_value = ""

        Button(
            width=17,
            height=4,
            text="(",
            relief="flat",
            bg="white",
            command=lambda: show("("),
        ).place(x=0, y=50)
        Button(
            width=17,
            height=4,
            text=")",
            relief="flat",
            bg="white",
            command=lambda: show(")"),
        ).place(x=90, y=50)
        Button(
            width=17,
            height=4,
            text="%",
            relief="flat",
            bg="white",
            command=lambda: show("%"),
        ).place(x=180, y=50)
        Button(
            width=17,
            height=4,
            text="1",
            relief="flat",
            bg="white",
            command=lambda: show(1),
        ).place(x=0, y=100)
        Button(
            width=17,
            height=4,
            text="2",
            relief="flat",
            bg="white",
            command=lambda: show(2),
        ).place(x=90, y=100)
        Button(
            width=17,
            height=4,
            text="3",
            relief="flat",
            bg="white",
            command=lambda: show(3),
        ).place(x=180, y=100)
        Button(
            width=17,
            height=4,
            text="4",
            relief="flat",
            bg="white",
            command=lambda: show(4),
        ).place(x=0, y=150)
        Button(
            width=17,
            height=4,
            text="5",
            relief="flat",
            bg="white",
            command=lambda: show(5),
        ).place(x=90, y=150)
        Button(
            width=17,
            height=4,
            text="6",
            relief="flat",
            bg="white",
            command=lambda: show(6),
        ).place(x=180, y=150)
        Button(
            width=17,
            height=4,
            text="7",
            relief="flat",
            bg="white",
            command=lambda: show(7),
        ).place(x=0, y=200)
        Button(
            width=17,
            height=4,
            text="8",
            relief="flat",
            bg="white",
            command=lambda: show(8),
        ).place(x=90, y=200)
        Button(
            width=17,
            height=4,
            text="9",
            relief="flat",
            bg="white",
            command=lambda: show(9),
        ).place(x=180, y=200)
        Button(
            width=17,
            height=4,
            text="0",
            relief="flat",
            bg="white",
            command=lambda: show(0),
        ).place(x=0, y=250)
        Button(
            width=17,
            height=4,
            text=".",
            relief="flat",
            bg="white",
            command=lambda: show("."),
        ).place(x=90, y=250)
        Button(
            width=17,
            height=4,
            text="+",
            relief="flat",
            bg="white",
            command=lambda: show("+"),
        ).place(x=180, y=250)
        Button(
            width=17,
            height=4,
            text="-",
            relief="flat",
            bg="white",
            command=lambda: show("-"),
        ).place(x=0, y=300)
        Button(
            width=17,
            height=4,
            text="/",
            relief="flat",
            bg="white",
            command=lambda: show("/"),
        ).place(x=90, y=300)
        Button(
            width=17,
            height=4,
            text="*",
            relief="flat",
            bg="white",
            command=lambda: show("*"),
        ).place(x=180, y=300)
        Button(
            width=17, height=4, text="=", relief="flat", bg="white", command=solve
        ).place(x=0, y=350)
        Button(
            width=17, height=4, text="C", relief="flat", bg="white", command=clear
        ).place(x=90, y=350)


root = Tk()
calculator = Calculator(root)
root.mainloop()
