import tkinter as tk

root = tk.Tk()
root.title('Tip Calculator')

# some variables that I will need
cost = tk.StringVar()
cost.set(0.0)

title = tk.Label(root, text='Tip Calculator')
title.grid(row=1, column=1)

meal_cost_label = tk.Label(root, text='Meal Costs:')
meal_cost_label.grid(row=2, column=1)

meal_cost_entry = tk.Entry(root, textvariable=cost)
meal_cost_entry.grid(row=2, column=2)

root.mainloop()