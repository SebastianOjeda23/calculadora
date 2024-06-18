import tkinter as tk

import tkinter as tk


def update_display(num):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + num)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def clear_display():
    display.delete(0, tk.END)


root = tk.Tk()
root.title("Calculadora")


display = tk.Entry(root, width=35, borderwidth=5, font=("Arial", 18))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]


row_val = 1
col_val = 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=calculate).grid(row=row_val, column=col_val, columnspan=2)
    elif button == "C":
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=clear_display).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda button=button: update_display(button)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 18), command=clear_display).grid(row=row_val, column=col_val, columnspan=4)


root.mainloop()