from tkinter import *
#its only for png type image
root=Tk()
root.geometry("1300x500")
photo=PhotoImage(file="Python-Programming-Language.png")
a=Label(image=photo)
a.pack()
root.mainloop()