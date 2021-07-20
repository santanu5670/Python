class Employee:
    company="Google"
    def showdetails(self):
        print("This is a employee")
class programmer(Employee):
    language="Python"
    def getdetails(self):
        print(f"The language is {self.language}")
e=Employee()
print(e.company)
e.showdetails()
p=programmer()
print(p.language)
p.getdetails()
print(p.company)
p.showdetails()