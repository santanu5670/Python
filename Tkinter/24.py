from tkinter import *
class GUI(Tk):
    def __init__(self): # Here self is use as a root
        super().__init__()
        self.geometry('644x344')
        self.title("Tkinter Using Class")
    def status(self):
        self.statusvar=StringVar()
        self.statusvar.set("Ready")
        self.sbar=Label(self,textvariable=self.statusvar,relief=SUNKEN,anchor='w')
        self.sbar.pack(side=BOTTOM,fill=X)
    def Button(self):
        Button(self,text="Upload",command=self.upload).pack()
    def upload(self):
        self.statusvar.set("Uploading..")
        self.sbar.update()
        import time
        time.sleep(2)
        self.statusvar.set("Ready")
if __name__=='__main__':
    window=GUI() #Here window is use as a root
    window.status()
    window.Button()
    window.mainloop()