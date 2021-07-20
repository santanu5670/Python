class Employee:
    company="Google"
    def getsalary(self):
        print(f"Salary for this company working in {self.company} is {self.salary}")
        # print(f"Salary for this company working in {dev.company} is {dev.salary}")
dev=Employee()
dev.salary=10000
dev.getsalary() 
#dev.getsalary converts into Employee.getsalary(dev) so we use self other wise getsalary() function 
#not take any parameter but Employee.getsalary(dev) takes 1 parameter
rajni=Employee()
rajni.salary=20000
Employee.getsalary(rajni)
