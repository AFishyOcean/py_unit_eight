import tkinter as tk

root = tk.Tk()
root.title('Calculator')
# variables
entry = tk.StringVar()

# make an entry box, give a text variable (entry (StringVar())
def press_three():
    text = entry.get()
    text += "3"
    entry.set(text)

# text box
entry_box = tk.Entry(root, text=entry)
entry_box.grid(row=1, column=1, columnspan=3)

# operations
add = tk.Button(root, text="+", )
add.grid(row=2, column=4)

subtract = tk.Button(root, text="-", )
subtract.grid(row=3, column=4)

multiply = tk.Button(root, text="x", )
multiply.grid(row=2, column=5)

divide = tk.Button(root, text="/", )
divide.grid(row=3, column=5)

calculate = tk.Button(root, text="=")
calculate.grid(row=4, column=5)

# numbers
num0 = tk.Button(root, text="0")
num0.grid(row=4, column=4)

num1 = tk.Button(root, text="1")
num1.grid(row=2, column=1)

num2 = tk.Button(root, text="2")
num2.grid(row=2, column=2)

num3 = tk.Button(root, text="3", command=press_three)
num3.grid(row=2, column=3)

num4 = tk.Button(root, text="4")
num4.grid(row=3, column=1)

num5 = tk.Button(root, text="5")
num5.grid(row=3, column=2)

num6 = tk.Button(root, text="6")
num6.grid(row=3, column=3)

num6 = tk.Button(root, text="7")
num6.grid(row=4, column=1)

num7 = tk.Button(root, text="8")
num7.grid(row=4, column=2)

num9 = tk.Button(root, text="9")
num9.grid(row=4, column=3)


root.mainloop()
