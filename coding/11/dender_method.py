class Number:
    def __init__(self,num,num1):
        self.num=num
        self.num1=num1
    def __str__(self):
        return f"The number is {self.num}"
    def __len__(self):
        return len(self.num1)
n=Number(9,"Hello")
print(n)
print(len(n))