list1=[1,2,3,4,5,6,7,8,9]
def is_grater_5(num):
    return num>5
max_5=list(filter(is_grater_5,list1))
print(max_5)
