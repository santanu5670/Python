class Employee:
    comapny="Google" #class attribute
    salary=100
rajni=Employee()
dev=Employee()
bikash=Employee()
rajni.salary=300 #instance attribute
dev.salary=400 #instance attribute
print(rajni.comapny)
print(rajni.salary)
print(dev.comapny)
print(dev.salary)
print(bikash.comapny)
print(bikash.salary) 
#Here salary is print 100 because we did not create instance attribute for bikash so it search is there any 
# class attribute present if present then print it otherwise throw an error
Employee.comapny="Youtube"
print(rajni.comapny)
print(dev.comapny)
