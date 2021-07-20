class Employee:
    company="Camel"
    Salary=100
    location="Delhi"
    def changesalary(self,sal):
        self.Salary=sal
    def changelocation(self,loc):
        self.__class__.location=loc 
        '''if we want to change the value of location in whole class and if we dont want to create any instance
        variable means value of class variable change then use __class__'''
e=Employee()
print(e.Salary)
print(e.location)
e.changesalary(500)
e.changelocation("Kolkata")
print(e.Salary)
print(e.location)
print(Employee.Salary)
''' self.Salary is a instance attribute so it change for object e not for the whole class '''
print(Employee.location)
f=Employee()
print(f.Salary)
''' for object f we did not initilize the method change salary so it print the value of class attribute salary'''
print(f.location)