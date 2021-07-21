from tkinter import *
def upload():
    statusvar.set("Uploading..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")
root=Tk()
root.title('Status Bar')
root.geometry('644x344')
statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor='w')
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Upload",command=upload).pack()
root.mainloop()