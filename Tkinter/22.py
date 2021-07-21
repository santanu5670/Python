from tkinter import *
root=Tk()
root.title('Scroolbar')
root.geometry('644x344')
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
# listbox=Listbox(root,yscrollcommand=scrollbar.set)
# for i in range(344):
#     listbox.insert(END,f"Item{i}")
# listbox.pack(fill="both")
# scrollbar.config(command=listbox.yview)
text=Text(root,yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)
root.mainloop()

#For connecting Scrollbar
# 1. Widget(yscrollcommand=scrollbar.set)
# 2.Scrollbar.config(command=Widget.yview)
