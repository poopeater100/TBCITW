from tkinter import *
from random import choice
root = Tk()
root.title("TBCITW")
root.geometry('340x800')
root.resizable (0,0)
Label(
    root,
    text=("This is the Best Checklist in the World")
    ).place (x=0, y=0)
    
#Buttons
button1=Button(root, text=" + ")
button1.place(x=10, y=29)

button2=Button(root, text = " - ")
button2.place(x=50, y=29)

button3=Button(root, text="view")
button3.place(x=90, y=29)

button4=Button(root, text="colors")
button4.place(x=141, y=29)

canvas=Canvas(
    root,
    bg="#000000",
    width=340, 
    height=2,);canvas.place(x=-2, y=60)
#canvas.create_line(140,0,140,400, fill="white", width=2)

root.mainloop()