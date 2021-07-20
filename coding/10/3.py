class attribute:
    a=10
obj=attribute()
obj.a=12
print(obj.a)
print(attribute.a)
obj1=attribute()
print(obj1.a)
'''we can not change the value of a by object in whole class because it is a 
 class attribute it can change the value of a for this object only to check print(Employee.a) and print(obj.a)'''