import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

#create a Tk() object that is the window
root_win = tk.Tk()

root_win.title("Criptosphere") # add a title to the window
root_win.iconbitmap("rasduino.ico")
root_win.geometry("600x370") #define the width and height of the window

# Let's add some widgets

lbl_heading = tk.Label(root_win, text="Criptoshere", font=("comic sans", 20, "italic"))
lbl_heading.grid(row=0, column=0)

criptoImage1 = ImageTk.PhotoImage(Image.open("criptoshere_V3_100px.png"))
criptoImage2= ImageTk.PhotoImage(Image.open("criptoshere_V3_250px.png"))
criptoImage3 = ImageTk.PhotoImage(Image.open("criptoshere_V3.png"))
criptoImage4 = ImageTk.PhotoImage(Image.open("criptoshere_V2_250px.png"))
criptoImage5 = ImageTk.PhotoImage(Image.open("criptoshere_V2_100px.png"))

image_list = [criptoImage1, criptoImage2, criptoImage3, criptoImage4, criptoImage5]

lbl_image = tk.Label(image=image_list[0])
lbl_image.grid(row=1, column=1, columnspan=3)

btn_back = tk.Button(root_win, text="<<")
btn_back.grid(row=2, column=0)
btn_forward = tk.Button(root_win, text=">>")
btn_forward.grid(row=2, column=3)


btn_exit = tk.Button(root_win, text="Exit", command=root_win.quit)
btn_exit.grid(row=2, column=2)

# create the loop event
root_win.mainloop()