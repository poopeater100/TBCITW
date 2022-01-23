from tkinter import *
from random import choice
root = Tk()

def plus():
    canvasplus=Canvas(root, width=1000, height=2, bg="#000000").place()

root.title("TBCITW")
root.geometry('340x800')
root.resizable (0,1)
#Label(root,text=("This is the Best Checklist in the World")).place (x=0, y=0)
    
#Buttons
button1=Button(root, text=" + ", padx=2, command=plus)
button1.place(x=10, y=10)

button2=Button(root, text = " - ", padx=3)
button2.place(x=50, y=10)

button3=Button(root, text="view")
button3.place(x=90, y=10)

button4=Button(root, text="colors")
button4.place(x=140, y=10)

canvas1=Canvas(
    root,
    bg="#000000",
    width=10000, 
    height=2,);canvas1.place(x=-2, y=40)
#canvas.create_line(140,0,140,400, fill="white", width=2)

root.mainloop()