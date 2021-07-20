class A:
    def __init__(self,c,d):
        self.a1=c
        self.b1=d
    def  add(self):
        self.c=self.a1+self.b1
        print("The addition is",self.c)

class B(A):
    def __init__(self, c, d):
        super().__init__(c,d)
        self.a2=c
        self.b2=d
    def sub(self):
        self.d=self.a2-self.b2
        print("The difference is=",self.d)

class C(B):
    def __init__(self, c, d):
        super().__init__(c, d)
        self.a3=c
        self.b3=d
    def mul(self):
        self.e=self.a3*self.b3
        print("The multiplication is",self.e)
class D(C):
    def __init__(self, c, d):
        super().__init__(c, d)
        self.a4=c
        self.b4=d
    def dev(self):
        self.f=self.a4//self.b4
        print("The Division is",self.f)
a=int(input("Enter First Number="))
b=int(input("Enter Second Number="))
obj=D(a,b)
obj.add()
obj.sub()
obj.mul()
obj.dev()