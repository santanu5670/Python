class Employee:
    company="Google"
    def getsalary(self,signature):
        print(f"Salary for this company working in {self.company} is {self.salary}\n{signature}")
        # print(f"Salary for this company working in {dev.company} is {dev.salary}")
    @staticmethod #static method help us to run function without self keyword
    #we can make many static method in a program 
    def greet():
        print("Good Evining Sir")
dev=Employee()
dev.salary=10000
dev.getsalary("Thanks!")
#dev.getsalary converts into Employee.getsalary(dev,"Thanks!") so we use self other wise getsalary() function 
#not take any parameter but Employee.getsalary(dev) takes 1 parameter
dev.greet() #  here greet() is a static method so it run as a Employee.greet().Here we have not need to pass 
# any object as a argument
rajni=Employee()
rajni.salary=20000
Employee.getsalary(rajni,"Thanks!")
Employee.greet()
