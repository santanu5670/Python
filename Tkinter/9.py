from tkinter import *
root=Tk()
root.geometry("444x222")
def hello():
    # print("Hello tkinter buttons")
    root1=Tk()
    root1.geometry("344x244")
    l1=Label(root1,text="Hello tkinter buttons")
    l1.pack(anchor=SW)
    root1.mainloop()
f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,anchor=NW)
b1=Button(f1,text="Print Now",fg="red",command=hello)
b1.pack(padx=20)
def name():
    print("VS Code")
f2=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f2.pack(side=RIGHT,anchor=NE)
b2=Button(f2,text="Print Now",fg="red",command=name)
b2.pack(padx=20)
f3=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f3.pack(side=BOTTOM,anchor=SW)
b3=Button(f3,text="Print Now",fg="red")
b3.pack(padx=20)
f4=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f4.pack(side=BOTTOM,anchor=SE)
b4=Button(f4,text="Print Now",fg="red")
b4.pack(padx=20)
root.mainloop()