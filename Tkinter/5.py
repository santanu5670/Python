#jpeg,jpg type of image are not supported in tkinter so first we have to install pillow
#command:-pip install pillow 
#then the following code for jpeg,jpg type of image
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("1200x600")
image=Image.open("python_image.jpeg")
photo=ImageTk.PhotoImage(image)
a=Label(image=photo)
a.pack()
b=Label(text="This is a Image of Python")
b.pack()
root.mainloop()