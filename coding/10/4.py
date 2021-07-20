class calculator:
    def square(self,a):
        return a*a
    def cube(self,a):
        return a*a*a
    def sqrt(self,a):
        return round(a**(1/2),2) #for two point decimal places
    @staticmethod
    def greet():
        print("Hello")
obj=calculator()
m=obj.square(5)
n=obj.cube(3)
o=obj.sqrt(8)
obj.greet()
print(f"The value of square is {m}")
print(f"The value of cube is {n}")
print(f"The value of square root is {o}")
