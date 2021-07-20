from tkinter import *
def myFile():
    print("Executing My File")
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

root.config(menu=mainmenu)

mainmenu.add_cascade(label="File",menu=m1)
mainmenu.add_cascade(label="Edit",menu=m2)
root.mainloop()