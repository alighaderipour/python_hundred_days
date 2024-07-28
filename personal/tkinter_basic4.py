import tkinter as tk

root = tk.Tk()
root.geometry("500x500")


def extra_sause():
    if chkbtnVar.get() == 0:
        entry2.delete(0, tk.END)
        entry2.insert(0, "not checked")
    else:
        entry2.delete(0, tk.END)
        entry2.insert(0, "checked")


chkbtnVar = tk.IntVar()
checkbutton = tk.Checkbutton(
    root,
    text="extra sauce",
    variable=chkbtnVar,
    command=extra_sause,
)
checkbutton.pack(pady=10)

entry = tk.Entry(root, textvariable=chkbtnVar)
entry.pack(pady=10)

entry2 = tk.Entry(root)
entry2.pack(pady=10)

root.title("Python Hundred Days")
root.resizable(False, False)
root.mainloop()
