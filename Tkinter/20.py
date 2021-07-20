from tkinter import *
import tkinter.messagebox as tmsg
def order():
    tmsg.showinfo("Order Received",f"We have received your order {var.get()}")
root=Tk()
root.title('Radio Button')
root.geometry('644x344')
# Use this if we want to pass integer value
# var=IntVar()
# Label(root,text="What would you like to have sir?",font="lucida 19 bold",justify=LEFT,padx=14).pack()
# radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value=1).pack(anchor="w")
# radio=Radiobutton(root,text="Idly",padx=14,variable=var,value=2).pack(anchor="w")
# radio=Radiobutton(root,text="Paratha",padx=14,variable=var,value=3).pack(anchor="w")
# radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value=4).pack(anchor="w")
# Button(text="Submit",command=order).pack()
# Use this if we want to pass string value
var=StringVar()
var.set("Radio")
Label(root,text="What would you like to have sir?",font="lucida 19 bold",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value="Idly").pack(anchor="w")
radio=Radiobutton(root,text="Paratha",padx=14,variable=var,value="Parata").pack(anchor="w")
radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value="Samosa").pack(anchor="w")
Button(text="Submit",command=order).pack()
root.mainloop()