from tkinter import *
import tkinter.messagebox as tmsg
def getdollars():
    tmsg.showinfo("Dollars",f"We have credited {myslider.get()} dollars into your bank account")
root=Tk()
root.title("Slider")
root.geometry('644x244')
# myslider=Scale(root,from_=0,to=455)
# myslider.pack()
Label(root,text="How many dollar do you want").pack()
myslider=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
# myslider=Scale(root,from_=20,to=455,orient=HORIZONTAL)
myslider.set(200) #if we want to set an default value 
myslider.pack()
Button(root,text="Get Dollars!",command=getdollars).pack()
root.mainloop()