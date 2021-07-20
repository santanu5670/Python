class Employee:
    def __init__(self,salary,increment):
        self.salary=salary
        self.increment=increment
    @property
    def salaryAfterIncrement(self):
        self.salary_increment=self.salary*self.increment
        return self.salary_increment
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,change_increment):
        self.increment=change_increment
salary=int(input("Enter the Salary of an Employee = "))
increment=int(input("Enter the increment of an Employee = "))
e=Employee(salary,increment)
print("Print salary with increment",e.salaryAfterIncrement)
ch=input("Do you want to change the increment Y/N :").upper()
if ch=='Y':
    change_increment=int(input("Enter the new increment value = "))
    print("Previous Salary with increment :",e.salaryAfterIncrement)
    print("Previous increment : ",e.increment)
    e.salaryAfterIncrement=change_increment
    print("New Salary with increment",e.salaryAfterIncrement)
    print("New increment : ",change_increment)
elif ch=='N':
    print("Bye")
else:
    print("Wrong cholice! Choose Y or N")

    