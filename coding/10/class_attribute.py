class Employee:
    comapny="Google"
rajni=Employee()
dev=Employee()
print(rajni.comapny)
print(dev.comapny)
Employee.comapny="Youtube"
print(rajni.comapny)
print(dev.comapny)
