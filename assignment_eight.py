import tkinter as tk

root = tk.Tk()
root.title('Calculator')
#variables


#make an entry box, give a text variable (entry (StringVar())
def press_three():
    text =entry.get()
    text += "3"
    entry.set(text)

#operations
add = tk.Button(root, text="+", )
add.grid(row=, column=, columnspan=)

subtract = tk.Button(root, text="-", )
subtract.grid(row=, column=, columnspan=)

multiply = tk.Button(root, text="x", )
multiply.grid(row=, column=, columnspan=)

divide = tk.Button(root, text="/", )
divide.grid(row=, column=, columnspan=)

calculate = tk.Button(root, text="=", command=)
calculate.grid(row=, column=, columnspan=)

#numbers
calculate = tk.Button(root, text="0", command=)
calculate.grid(row=, column=, columnspan=)

calculate = tk.Button(root, text="1", command=)
calculate.grid(row=, column=, columnspan=)

calculate = tk.Button(root, text="2", command=)
calculate.grid(row=, column=, columnspan=)

calculate = tk.Button(root, text="3", command=)
calculate.grid(row=, column=, columnspan=)

calculate = tk.Button(root, text="4", command=)
calculate.grid(row=, column=, columnspan=)

calculate = tk.Button(root, text="5", command=)
calculate.grid(row=, column=, columnspan=)

calculate = tk.Button(root, text="6", command=)
calculate.grid(row=, column=, columnspan=)

calculate = tk.Button(root, text="7", command=)
calculate.grid(row=, column=, columnspan=)

calculate = tk.Button(root, text="8", command=)
calculate.grid(row=, column=, columnspan=)

calculate = tk.Button(root, text="9", command=)
calculate.grid(row=, column=, columnspan=)





root.mainloop()
