import tkinter as tk

root = tk.Tk()


def copy_text():
    content = textbox1.get(1.0, tk.END)
    myEntry.delete(0, tk.END)
    myEntry.insert(0, content)


def get_lable():
    content = label.cget("text")  # text="Hello World",
    textbox1.delete(1.0, tk.END)
    textbox1.insert(1.0, content + " students !!!!😍😍😍")


root.geometry("400x400")
root.title("Python Hundred Days")

label = tk.Label(root, text="Hello World", font=("Arial", 15))
label.pack(padx=10, pady=10)


textbox1 = tk.Text(root, height=5, width=10)
textbox1.pack(padx=10, pady=10)

myEntry = tk.Entry(root)
myEntry.pack(padx=10)

button = tk.Button(root, text="Click Me", command=get_lable)

button.pack()

button2 = tk.Button(root, text="Click Me", command=copy_text)
button2.pack()

root.mainloop()

"""
chon dar text ma chand line darim be khatere hamin avalin khat mishe 1
avalin index mishe 0
ebtedaye text mishe 1.0

baraye entry, chon 1 line hast hamishe, avalsh mishe 0
dige niazi nist benevisim 1.0 chon on 1 badihi hast
chon entry hamishe 1 line hast
"""
