import database as db
import mysql.connector
from tkinter import *

root=Tk()
root.title('Data Sheet')
root.geometry('644x344')
Label(root,text="Welcome to Travel Agency",font="comicsunsms 19 bold",pady=15).grid(row=0,column=2)
name=Label(root,text="Name")
phone=Label(root,text="Phone Number")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency Contact")
payment=Label(root,text="Payment Mode")

name.grid(row=1,column=1)
phone.grid(row=2,column=1)
gender.grid(row=3,column=1)
emergency.grid(row=4,column=1)
payment.grid(row=5,column=1)

namevalues=StringVar()
phonevalues=StringVar()
gendervalues=StringVar()
emergencyvalues=StringVar()
paymentvalues=StringVar()
foodservicevalues=IntVar() #for checkbox

nameentry=Entry(root,textvariable=namevalues).grid(row=1,column=2)
phoneentry=Entry(root,textvariable=phonevalues).grid(row=2,column=2)
genderentry=Entry(root,textvariable=gendervalues).grid(row=3,column=2)
emergencyentry=Entry(root,textvariable=emergencyvalues).grid(row=4,column=2)
paymententry=Entry(root,textvariable=paymentvalues).grid(row=5,column=2)

foodservice=Checkbutton(text="Want to add meals?",variable=foodservicevalues)
foodservice.grid(row=6,column=2)
Button(text="Submit",command=db.data_insert,padx=10).grid(column=2)
root.mainloop()