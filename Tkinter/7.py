from tkinter import *
root=Tk()
root.geometry("644x444")
root.title("Frame")
f1=Frame(root,bg="grey",borderwidth=50,relief=SUNKEN)
f1.pack(side=LEFT)
l=Label(f1,text="Frame")
l.pack()
f2=Frame(root,bg="Orange",borderwidth=6,relief=GROOVE)
f2.pack(anchor=NW)
l1=Label(f2,text="Project")
l1.pack()
root.mainloop()