from tkinter import *
def get_values():
    # print(f"Foodservices: {foodservicevalues.get()}")
    with open ("records.txt","a") as f:
        f.write(f'''{namevalues.get(),phonevalues.get(),gendervalues.get(),emergencyvalues.get(),paymentvalues.get(),
                foodservicevalues.get()}\n ''')
        f.close()
root=Tk()
root.geometry("344x244")
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
Button(text="Submit",command=get_values,padx=10).grid(column=2)
root.mainloop()