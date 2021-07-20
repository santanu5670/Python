from tkinter import *
root=Tk()
root.geometry("344x244")
user=Label(root,text="Username")
password=Label(root,text="Password")
user.grid() #it is same as user.grid(row=0,column=0)
password.grid(row=1) #It is same as user.grid(row=1,column=0) 
# actually bydefault user.grid() means user.grid(row=0,column=0) so for row=0 or column=0 we have to specify it
uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
def getvalue():
    print("Data Submitted Successfully")
    print(f"Username is {uservalue.get()}")
    print(f"Password is {passvalue.get()}")
Button(text="Submit",command=getvalue).grid()
root.mainloop()
#variable classes in Tkinter:
# BooleanVar,DoubleVar,IntVar,StringVar