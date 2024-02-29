import tkinter as tk
from tkinter import ttk

root = tk.Tk()

ent_num = tk.Entry(root)
ent_num.pack()

def click ():
    lbl_out = tk.Label(root, text=ent_num.get())
    lbl_out.pack()
    
btn_click = tk.Button(root, text="click me", command=click)
btn_click.pack()

root.mainloop()