class Employee:
    company="Visa"
    eCode=120
class Freelancer:
    company="Fiverr"
    level=0
    def upgradelavel(self):
        self.level=self.level+1
        print(self.level)
class Programmer(Freelancer,Employee):
    name="Rohit"
 #here we take first Freelance so when we use print(p.company) then print Fiverr but if we use first Employee 
#like Programmer(Freelancer,Employee) then it will print visa
p=Programmer()
p.upgradelavel()
print(p.company)