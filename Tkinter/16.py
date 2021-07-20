# Change the windows screen according to the user specefied size
from tkinter import *
def update():
    root.geometry(f"{width.get()}x{hight.get()}")
root=Tk()
root.title("Windows Resizer")
root.geometry("344x244")
width=StringVar()
hight=StringVar()
Entry(root,textvariable=width).pack()
Entry(root,textvariable=hight).pack()
Button(root,text="Apply",command=update).pack()
root.mainloop()