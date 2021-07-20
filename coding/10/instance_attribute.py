class Employee:
    comapny="Google" #class attribute
rajni=Employee()
dev=Employee()
rajni.salary=300 #instance attribute
dev.salary=400 #instance attribute
print(rajni.comapny)
print(rajni.salary)
print(dev.comapny)
print(dev.salary)
Employee.comapny="Youtube"
print(rajni.comapny)
print(dev.comapny)
