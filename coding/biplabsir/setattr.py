class student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
s1=student('Rajesh',1,20)
s2=student('Ramesh',2,21)
setattr(s1,"id",22)
print(getattr(s1,'name'))
print(getattr(s2,'name'))
print(s1.id)


