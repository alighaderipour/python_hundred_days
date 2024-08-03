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

        def show(self, value):
            self.entry_value += str(value)
            self.equation.set(self.entry_value)

        def clear(self):
            self.entry_value = ""
            self.equation.set(self.entry_value)

        def solve():
            result = eval(self.entry_value)
            self.equation.set(result)

        Button(
            width=17,
            height=4,
            text="(",
            relief="flat",
            bg="white",
            command=lambda: self.show("(").place(x=0, y=50),
        )
        Button(
            width=17,
            height=4,
            text=")",
            relief="flat",
            bg="white",
            command=lambda: self.show(")").place(x=90, y=50),
        )
        Button(
            width=17,
            height=4,
            text="%",
            relief="flat",
            bg="white",
            command=lambda: self.show("%").place(x=180, y=50),
        )
        Button(
            width=17,
            height=4,
            text="1",
            relief="flat",
            bg="white",
            command=lambda: self.show(1).place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="2",
            relief="flat",
            bg="white",
            command=lambda: self.show(1).place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="3",
            relief="flat",
            bg="white",
            command=lambda: self.show(3).place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="4",
            relief="flat",
            bg="white",
            command=lambda: self.show(4).place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="5",
            relief="flat",
            bg="white",
            command=lambda: self.show(5).place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="6",
            relief="flat",
            bg="white",
            command=lambda: self.show(6).place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="7",
            relief="flat",
            bg="white",
            command=lambda: self.show(7).place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="8",
            relief="flat",
            bg="white",
            command=lambda: self.show(8).place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="9",
            relief="flat",
            bg="white",
            command=lambda: self.show(9).place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="0",
            relief="flat",
            bg="white",
            command=lambda: self.show(0).place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text=".",
            relief="flat",
            bg="white",
            command=lambda: self.show(".").place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="+",
            relief="flat",
            bg="white",
            command=lambda: self.show("+").place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="-",
            relief="flat",
            bg="white",
            command=lambda: self.show("-").place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="/",
            relief="flat",
            bg="white",
            command=lambda: self.show("/").place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="*",
            relief="flat",
            bg="white",
            command=lambda: self.show("*").place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="=",
            relief="flat",
            bg="white",
            command=self.solve().place(x=0, y=0),
        )
        Button(
            width=17,
            height=4,
            text="C",
            relief="flat",
            bg="white",
            command=self.clear().place(x=0, y=0),
        )


root = Tk()
calculator = Calculator(root)
root.mainloop()