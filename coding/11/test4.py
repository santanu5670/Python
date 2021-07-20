class Employee:
    def addEmployee(self,name,id,age,gender):
        self.name=name
        self.id=id
        self.age=age
        self.gender=gender
class Organisation(Employee):
    def __init__(self,name_organization,employees):
        self.name_organization=name_organization
        self.employees=employees
    def addEmployee(self,name,id,age,gender):
        super().addEmployee(name,id,age,gender)
        # self.name=name
        # self.id=id
        # self.age=age
        # self.gender=gender
        self.employees.append([self.name,self.id,self.age,self.gender])
    def getEmployeeCount(self):
        return len(self.employees)
        # return self.employees[1][0]
    def findEmployeeAge(self,id):
        self.id=id
        for i in range(0,len(self.employees)):
            for j in range(0,4):
                if self.employees[i][j]==self.id:
                    return self.employees[i][j+1]
        else:
            return -1
    def countEmployees(self,age):
        self.count=0
        self.age=age
        for i in range(0,len(self.employees)):
            if self.employees[i][2]>self.age:
                self.count=self.count+1
        return self.count
                

if __name__ == '__main__':
    employees=[]
    o = Organisation('XYZ',employees)
    n=int(input())
    for i in range(n):
        name=input()
        id=int(input())
        age=int(input())
        gender=input()
        o.addEmployee(name,id,age,gender)

    id=int(input())
    age=int(input())
    print(o.getEmployeeCount())
    print(o.findEmployeeAge(id))
    print(o.countEmployees(age))

#     1
# AAA
# 123
# 25
# M
# 120