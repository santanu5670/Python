class Employee:
    Company="Bharat Gas"
    Salary=5500
    bonus=500
    
    @property
    def totalsalary(self):
        return self.Salary+self.bonus
    
    @totalsalary.setter
    def totalsalary(self,val):
        self.bonus=val-self.Salary

e=Employee()
print("Previous Total Salary",e.totalsalary) #here totalsalary is behave like a property.It is also know as a getter
print("Previous bonus",e.bonus)
e.totalsalary=5800
print(e.Salary)
print("New Bonus",e.bonus)
print("New Total Salary",e.totalsalary)