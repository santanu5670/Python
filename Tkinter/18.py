from tkinter import *
import tkinter.messagebox as tmsg
def myFile():
    print("Executing My File")
def help():
    # a=tmsg.Message("This is a help option")
    a=tmsg.showinfo("Help","We Will Help You With This GUI")
    print(a) # It will print return value
def rateus():
    val=tmsg.askquestion("Your Experience","Was Your Experience Good?")
    print(val)
    if val=='yes':
        msg="Great Please Rate Us On Our WebSite"
    else:
        msg="Tell us what problem you faced.We will try resolved it soon"
    tmsg.showinfo("Experience",msg)
def warning():
    ans=tmsg.askretrycancel("Warning","It will Not work")
    if ans:
        print("Don't don this other wise it will close parmanently")
    else:
        print("Great for Back")
root=Tk()
root.title('VS Code')
root.geometry('644x344')
# Use this to Create non-dropdown menu :-
# mymenu=Menu(root)
# mymenu.add_command(label="File",command=myFile)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)
# Use this to create a drop-down menu:-
mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0) # tearoff is used to remove the doted line in menu
m1.add_command(label="New File",command=myFile)
m1.add_command(label="New Window",command=myFile)
m1.add_separator() # It is used to add a line between menu 
m1.add_command(label="Save",command=myFile)
m1.add_command(label="Save As",command=myFile)
m1.add_separator() # It is used to add a line between menu
m1.add_command(label="Exit",command=quit)

m2=Menu(root)
m2.add_command(label="Undo",command=myFile)
m2.add_command(label="Redo",command=myFile)

m3=Menu(root,tearoff=0)
m3.add_command(label="help",command=help)
m3.add_command(label="Rate Us",command=rateus)
m3.add_command(label="Warning",command=warning)


root.config(menu=mainmenu)

mainmenu.add_cascade(label="File",menu=m1)
mainmenu.add_cascade(label="Edit",menu=m2)
mainmenu.add_cascade(label="Help",menu=m3)
root.mainloop()