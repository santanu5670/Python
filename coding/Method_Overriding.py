class A:
    def display(self,a=None,b=None):
        if a!=None and b!=None:
            print("The values are",a,b)
        elif a!=None:
            print("The value is",a)
        else:
            print("Hello, How are You")
obj=A()
obj.display()
obj.display(5)
obj.display("Amit Kumar")
obj.display(4,5)


