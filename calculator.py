import tkinter as tk
from tkinter import ttk

btn_wd = 30
btn_ht = 15



win_calc = tk.Tk()

win_calc.title("Calculator")

lbl_AppName = tk.Label(win_calc, text=" Calculator  ", font=("comic sans", 40, "italic"), fg="green", bg="orange")
lbl_AppName.grid(row=0, column=0, columnspan=4)

ent_numbers = tk.Entry(win_calc, border=5, width=48)
ent_numbers.grid(row=1, column=0, columnspan=4)

def numPad(number):
    current = ent_numbers.get()
    ent_numbers.delete(0, tk.END)
    ent_numbers.insert(0,str(current)+str(number))
    
def clear():
    ent_numbers.delete(0, tk.END)
    
def add():
    val = int(ent_numbers.get())
    ent_numbers.delete(0, tk.END)
    val = val + 10
    ent_numbers.insert(0, val)

btn_num7 = tk.Button(win_calc, text="7", padx=30, pady=btn_ht, command=lambda: numPad(7))
btn_num7.grid(row=3, column=0)
btn_num8 = tk.Button(win_calc, text="8", padx=30, pady=btn_ht, command=lambda: numPad(8))
btn_num8.grid(row=3, column=1)
btn_num9 = tk.Button(win_calc, text="9", padx=30, pady=btn_ht, command=lambda: numPad(9))
btn_num9.grid(row=3, column=2)
btn_mult = tk.Button(win_calc, text="x", padx=29, pady=btn_ht)
btn_mult.grid(row=3, column=3)

btn_num4 = tk.Button(win_calc, text="4", padx=30, pady=btn_ht, command=lambda: numPad(4))
btn_num4.grid(row=4, column=0)
btn_num5 = tk.Button(win_calc, text="5", padx=30, pady=btn_ht, command=lambda: numPad(5))
btn_num5.grid(row=4, column=1)
btn_num6 = tk.Button(win_calc, text="6", padx=30, pady=btn_ht, command=lambda: numPad(6))
btn_num6.grid(row=4, column=2)
btn_div = tk.Button(win_calc, text="/", padx=30, pady=btn_ht)
btn_div.grid(row=4, column=3)

btn_num1 = tk.Button(win_calc, text="1", padx=30, pady=btn_ht, command=lambda: numPad(1))
btn_num1.grid(row=5, column=0)
btn_num2 = tk.Button(win_calc, text="2", padx=30, pady=btn_ht, command=lambda: numPad(2))
btn_num2.grid(row=5, column=1)
btn_num3 = tk.Button(win_calc, text="3", padx=30, pady=btn_ht, command=lambda: numPad(3))
btn_num3.grid(row=5, column=2)
btn_add = tk.Button(win_calc, text="+", padx=28, pady=btn_ht, command=add)
btn_add.grid(row=5, column=3)

btn_num0 = tk.Button(win_calc, text=" 0", padx=66, pady=btn_ht)
btn_num0.grid(row=6, column=0, columnspan=2)
btn_clr = tk.Button(win_calc, text="C", padx=30, pady=btn_ht, command=clear)
btn_clr.grid(row=6, column=2)
btn_sbtr = tk.Button(win_calc, text="-", padx=30, pady=btn_ht)
btn_sbtr.grid(row=6, column=3)

win_calc.mainloop()