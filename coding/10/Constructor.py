class Employee:
    company="Google"
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print(type(self.salary))
        print("Employee is created")
    def getDetails(self):
        self.a=100
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
    def getsalary(self,signature):
        print(self.a)
        print(f"Salary for this company working in {self.company} is {self.salary}\n{signature}")
    @staticmethod 
    def greet():
        print("Good Evining Sir")
dev=Employee("Dev",100,"Youtube")
dev.getDetails()
dev.getsalary("Thanks!")
dev.greet()
print(dev.name)
dev.name="Satyajit"
print(dev.name)
