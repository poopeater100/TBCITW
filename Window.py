from tkinter import *
from random import choice
root = Tk()
root.title("TBCITW")
root.geometry('340x800')
root.resizable (0,0)
Label(
    root,
    text=("Checklist")
    ).pack ()

canvas=Canvas(
    root,
    bg="#000000",
    width=340, 
    height=790,);canvas.pack()

canvas.create_line(140,0,140,400, fill="white", width=2)
root.mainloop()