import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculator")

def insert(num):
    entry.insert(tk.END, num)

    return

def calculate():
    SpecialChar = ["%",]
    entry_text = entry.get()
    index = 0

    for char in entry_text:
        if char in SpecialChar:
            entry_text = entry_text[:index] + "/100" + entry_text[index+1:]
        index += 1

    if entry_text != "" :
        try:
            result = str(eval(entry_text))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
        return
    else:
        return

def AllClear():
    entry.delete(0, tk.END)

    return

def backspace():
    try:
        entry.delete(len(entry.get())-1, tk.END)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "")

    return

def sign_change():
    operators = ['+', '-', '*', '/', '%']
    text = entry.get()

    if not text:
        return

    for pos in range(len(text)-1, -1, -1):
        char = text[pos]
        if char in operators:
            if char == '+' :
                text = text[:pos] + '-' + text[pos+1:]
            elif char == '-' :
                text = text[:pos] + '+' + text[pos+1:]
            else:
                text = text[:pos+1] + '-' + text[pos+1:]
            entry.delete(0, tk.END)
            entry.insert(0, text)
            return

    if text.startswith('-'):
        text = text[1:]
    else:
        text = '-' + text
    entry.delete(0, tk.END)
    entry.insert(0, text)

    
        

entry = ttk.Entry(root, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons =[
    'AC', '<=', '+/-', '/', 
    '1' , '2' , '3'  , '*', 
    '4' , '5' , '6'  , '-', 
    '7' , '8' , '9'  , '+', 
    '%' , '0' , '.'  , '='
]

for button in buttons:
    if button == 'AC':
        ttk.Button(root, text=button, command=AllClear).grid(row=buttons.index(button)//4 + 1, column=buttons.index(button)%4, padx=5, pady=5, sticky="nsew")
    elif button == '<=':
        ttk.Button(root, text=button, command=backspace).grid(row=buttons.index(button)//4 + 1, column=buttons.index(button)%4, padx=5, pady=5, sticky="nsew")
    elif button == '+/-':
        ttk.Button(root, text=button, command=sign_change).grid(row=buttons.index(button)//4 + 1, column=buttons.index(button)%4, padx=5, pady=5, sticky="nsew")
    elif button == '=':
        ttk.Button(root, text=button, command=calculate).grid(row=buttons.index(button)//4 + 1, column=buttons.index(button)%4, padx=5, pady=5, sticky="nsew")
    else:
        ttk.Button(root, text=button, command=lambda b=button: insert(b)).grid(row=buttons.index(button)//4 + 1, column=buttons.index(button)%4, padx=5, pady=5, sticky="nsew")

for row in range(7):
    root.rowconfigure(row, weight=1)
for col in range(4):
    root.columnconfigure(col, weight=1)

root.mainloop()

