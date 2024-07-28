import tkinter as tk


def show_selection():
    if var.get() == 1:
        label.config(text="Checkbutton is checked")
    else:
        label.config(text="Checkbutton is unchecked")


root = tk.Tk()
root.geometry("300x200")
root.title("Checkbutton Example")

var = tk.IntVar()

checkbutton = tk.Checkbutton(
    root, text="Check me", variable=var, command=show_selection
)
checkbutton.pack(pady=20)

label = tk.Label(root, text="Checkbutton is unchecked", font=("Arial", 12))
label.pack(pady=20)

root.mainloop()
