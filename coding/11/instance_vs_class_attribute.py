class Employee:
    company="Camel"
    Salary=100
    location="Delhi"
    def changesalary(self,sal):
        self.Salary=sal
e=Employee()
print(e.Salary)
e.changesalary(500)
print(e.Salary)
print(Employee.Salary)
''' self.Salary is a instance attribute so it change for object e not for the whole class '''
f=Employee()
print(f.Salary)
''' for object f we did not initilize the method change salary so it print the value of class attribute salary'''