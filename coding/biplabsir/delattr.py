class student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
s1=student('Rajesh',1,20)
s2=student('Ramesh',2,21)
print(getattr(s1,'name'))
print(getattr(s2,'name'))
delattr(s1,"id") # it is used to delete a attribute for particular object
print(hasattr(s1,"age"))
print(hasattr(s1,"id")) # now check id is present for s1 or not
print(hasattr(s1,"id")) # also check id is present for s2 or not



