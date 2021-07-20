from tkinter import *
root=Tk()
canvas_width=400
canvas_hight=200
root.geometry(f"{canvas_width}x{canvas_hight}")
# can_widget=Canvas(root,width=canvas_width,height=canvas_hight)
# can_widget=Canvas(root,width=canvas_width,height=canvas_hight)
can_widget=Canvas(root,width=1200,height=1200)
can_widget.pack()
#The lines goes from the point x1,y1,x2,y2
can_widget.create_line(0,0,800,400,fill='red')
can_widget.create_line(0,400,800,0,fill='red')
can_widget.create_line(0,200,800,200,fill='red')
can_widget.create_line(400,0,400,400,fill='red')
#To create ractangle specify parameter in this order:- corner of the top left and corner of the buttom right
# can_widget.create_rectangle(3,5,700,300,fill="blue")
can_widget.create_text(200,200,text="Python")
#To create oval specify parameter in this order:- corner of the top left and corner of the buttom right
can_widget.create_oval(344,233,244,355)
root.mainloop()