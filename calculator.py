# Tkinter Calculator
# Author: <Itisha Chouhan>

import tkinter as tk 


# ---------- Functions (what happens when buttons are clicked) ----------

def press(value):
    """Add the clicked digit/operator to the end of the display."""
    entry.insert(tk.END, value)


def clear():
    """Wipe everything from the display."""
    entry.delete(0, tk.END)


def calculate():
    """Read the expression, evaluate it, and show the result."""
    expression = entry.get()
    try:
        result = eval(expression)          
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Cannot divide by 0")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# ---------- Window ----------

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

# ---------- Display (Entry widget) ----------

entry = tk.Entry(root, font=("Arial", 24), justify="right", bd=8, relief="sunken")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=8)

# ---------- Buttons ----------
# Each row of the keypad is a list of button labels.

layout = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
]

for r, row in enumerate(layout, start=1):       
    for c, label in enumerate(row):
        if label == "C":
            cmd = clear
        elif label == "=":
            cmd = calculate
        else:
            cmd = lambda v=label: press(v)    
        tk.Button(
            root, text=label, font=("Arial", 18), width=4, height=2, command=cmd
        ).grid(row=r, column=c, padx=4, pady=4)

# ---------- Start the app ----------

root.mainloop()
