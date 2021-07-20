numbers=['3','33','66']
'''for i in range(len(numbers)):
    numbers[i]=int(numbers[i])
numbers[2]=numbers[2]+1
print(numbers[2])'''
#or
'''s=[]
for items in numbers:
    items=int(items)
    s.append(items)
print(s)
print(numbers)
s[2]=s[2]+1
print(s[2])'''

#Using Map

num=list(map(int,numbers))
print(num)
num[2]=num[2]+1
print(num[2])

