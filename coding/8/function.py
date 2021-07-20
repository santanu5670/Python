# marks1=[45,78,60,90]
# percentage1=(sum(marks1)/400)*100
# print(percentage1)

# marks2=[55,70,65,95]
# percentage2=(sum(marks2)/400)*100
# print(percentage2)

# We can do this using function it is more benificial for us

def percent(marks):
    p=(sum(marks)/400)*100
    return p
marks1=[45,78,60,90]
print(percent(marks1))