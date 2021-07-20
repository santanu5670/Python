class Number:
    def __init__(self,num): #This type of method is called dender method
        self.num=num
        # print(num)
    def __add__(self,num2): #This type of method is called dender method
        return self.num+num2.num
        # print(num2.num)
    def __mul__(self,num2): #This type of method is called dender method
        # return self.num*num2.num
        print(num2)
        print(self)
n1=Number(4)
n2=Number(6)
print(n2)
print(n1)
sum=n1+n2
print(sum)
mul=n1*n2
print(mul)