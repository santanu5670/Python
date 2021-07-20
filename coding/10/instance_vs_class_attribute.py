class Employee:
    company="Google"
    def putData(self):
        self.name="Rajesh" # It is a instance attribute because it can not access by print(Employee.name) where
        # Employee is a class name but object can able to access it
        self.Id=1
        self.a=100
    # def Getinfo(self):
    #     print(f"Name is {self.name} and Employee id is {self.Id} and company is {self.company}")
    #     print(self.a)
dev=Employee()
dev.name="Dev"
dev.company="Youtube" 
'''we can not change the value of company by object in whole class because it is a 
 class attribute it can change the value of company for this object only to check print(Employee.company)'''
dev.salary=100
print(dev.name)
print(dev.company) #comapany is a class attribute which can accessible by object name also by class name
print(Employee.company) #comapany is a class attribute which can accessible by class name also
print(dev.salary) #salary is a instance attribute which can accessible by object name but not by class name 
# print(Employee.salary) #salary is a instance attribute which can not accessible by class name
print(Employee.name)
'''name,slalry,id are instance attribute because it can not access by print(Employee.name) where
Employee is a class name but object can able to access it.'''

'''We know class attribute can access by Employee.attribute_name like Employee.company is accessible 
or class attribute also accessble by object.attribute_name like dev.company but instance attribute are 
not accessible by class name so we can not access it by Employee.attribute_name like Employee.name but 
instance attribute are accessible by object name like dev.name so we can say that self.name,self.id are 
instance attribute.''' 
