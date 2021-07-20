def click(event):
    # The below line tell us in which position we clicked the mouse at window
    print(f"You clicked on the button at {event.x} and {event.y}")
from tkinter import *
root=Tk()
root.title("Events")
root.geometry('644x344')
widget=Button(root,text="Clicked On Me")
widget.pack()
widget.bind('<Button-1>',click)
widget.bind('<Double-1>',quit)
root.mainloop()