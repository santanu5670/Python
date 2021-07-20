from tkinter import *
root=Tk()
root.geometry("644x344")
root.title("My GUI")
text_label=Label(text='''Python is an interpreted high-level general-purpose programming language. Python's
design philosophy emphasizes code readability with its notable use of significant indentation. Its language 
constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small
and large-scale projects.[30]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including 
structured (particularly, procedural), object-oriented and functional programming. Python is often described 
as a "batteries included" language due to its comprehensive standard library.[31]

Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, 
and first released it in 1991 as Python 0.9.0.[32] Python 2.0 was released in 2000 and introduced new features,
such as list comprehensions and a garbage collection system using reference counting. Python 3.0 was released 
in 2008 and was a major revision of the language that is not completely backward-compatible and much Python 2 
code does not run unmodified on Python 3. Python 2 was discontinued with version 2.7.18 in 2020.[33]''' 
,bg='red',fg="blue",padx=44,pady=60,font="comicsansms 10 bold",borderwidth=5, relief=SUNKEN)
# text_label.pack(anchor=NW)
# text_label.pack(anchor=NE)
#FOR SW and SE we have add side="buttom"
# text_label.pack(side="bottom",anchor=SE)
# text_label.pack(side="bottom",anchor=SW)
# text_label.pack(side="bottom")
# text_label.pack(side="bottom",anchor=SE,fill=X)
# text_label.pack(side="left")
text_label.pack(side="right",fill=Y,padx=34,pady=24)
root.mainloop()

#Important Label Option
'''
text-add text
bd-background
fg-foreground
font-sets the font:-
first way to set a font: font=("comicsansms",10,"bold")
second way to set a font: font="comicsansms 10 bold"
padx-x padding
pady- y padding
relief- border styling -SUNKEN,RAISED,GROOVE,RIDGE 
'''
#Important pack option
'''
anchor-NW,NE,SW,SE(NW-NORTH WEST,NE-NORTH EAST,SE-SOUTH EAST,NW-NORTH WEST)
'''