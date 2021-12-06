import tkinter as tk

root = tk.Tk()
root.title('Calculator')
# variables
entry = tk.StringVar()

# make an entry box, give a text variable (entry (StringVar())
def press_zero():
    text = entry.get()
    text += "0"
    entry.set(text)
def press_one():
    text = entry.get()
    text += "1"
    entry.set(text)
def press_two():
    text = entry.get()
    text += "2"
    entry.set(text)
def press_three():
    text = entry.get()
    text += "3"
    entry.set(text)
def press_four():
    text = entry.get()
    text += "4"
    entry.set(text)
def press_five():
    text = entry.get()
    text += "5"
    entry.set(text)
def press_six():
    text = entry.get()
    text += "6"
    entry.set(text)
def press_seven():
    text = entry.get()
    text += "7"
    entry.set(text)
def press_eight():
    text = entry.get()
    text += "8"
    entry.set(text)
def press_nine():
    text = entry.get()
    text += "9"
    entry.set(text)
def press_add():
    text = entry.get()
    text += "+"
    entry.set(text)
def press_subtract():
    text = entry.get()
    text += "-"
    entry.set(text)
def press_multiply():
    text = entry.get()
    text += "*"
    entry.set(text)
def press_divide():
    text = entry.get()
    text += "/"
    entry.set(text)
# text box
entry_box = tk.Entry(root, text=entry)
entry_box.grid(row=1, column=1, columnspan=3)

# operations
add = tk.Button(root, text="+", command=press_add)
add.grid(row=2, column=4)

subtract = tk.Button(root, text="-", command=press_subtract)
subtract.grid(row=3, column=4)

multiply = tk.Button(root, text="x", command=press_multiply)
multiply.grid(row=2, column=5)

divide = tk.Button(root, text="/", command=press_divide)
divide.grid(row=3, column=5)

calculate = tk.Button(root, text="=")
calculate.grid(row=4, column=5)

# numbers
num0 = tk.Button(root, text="0", command=press_zero)
num0.grid(row=4, column=4)

num1 = tk.Button(root, text="1", command=press_one)
num1.grid(row=2, column=1)

num2 = tk.Button(root, text="2", command=press_two)
num2.grid(row=2, column=2)

num3 = tk.Button(root, text="3", command=press_three)
num3.grid(row=2, column=3)

num4 = tk.Button(root, text="4", command=press_four)
num4.grid(row=3, column=1)

num5 = tk.Button(root, text="5", command=press_five)
num5.grid(row=3, column=2)

num6 = tk.Button(root, text="6", command=press_six)
num6.grid(row=3, column=3)

num6 = tk.Button(root, text="7", command=press_seven)
num6.grid(row=4, column=1)

num7 = tk.Button(root, text="8", command=press_eight)
num7.grid(row=4, column=2)

num9 = tk.Button(root, text="9", command=press_nine)
num9.grid(row=4, column=3)


root.mainloop()



# eval("1+2") when doing =