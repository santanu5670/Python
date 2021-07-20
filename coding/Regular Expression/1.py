import re
nameage='''Jaince is 22 and Theon is 33
Gabriel is 44 and Joey is 21'''
print(nameage)
ages=re.findall(r'\d{1,3}',nameage)
print(ages)
names=re.findall(r'[A-Z][a-z]*',nameage)
print(names)

agedict={}
x=0
for eachname in names:
    agedict[eachname]=ages[x]
    x+=1
print(agedict)
