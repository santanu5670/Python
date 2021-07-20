class Programmer:
    company_name="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"The name of the employee is {self.name} and product is {self.product}")
name=input("Enter a name\n")
product=input("Enter a product\n")
dev=Programmer(name,product)
rajni=Programmer("Rajni","Github")
dev.getInfo()
rajni.getInfo()
