class student:
    def add(self,a,b):
        self.a=a
        self.b=b
        self.c=self.a+self.b
        print(self.c)
s=student()
s.add(10,20)