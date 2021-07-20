class Employee:
    company="Camel"
    Salary=100
    location="Delhi"
    @classmethod
    def changesalary(cls,sal):
        cls.Salary=sal
        ''' If we not want to create instance attribute or if we want change the value of salary in whole 
        class not only fro any particular object and if we also not want to use dunder methon the use class
        method '''
e=Employee()
print(e.Salary)
e.changesalary(500)
print(e.Salary)
print(Employee.Salary)
f=Employee()
print(f.Salary)