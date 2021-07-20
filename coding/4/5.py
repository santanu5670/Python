a=[1,2,3,4]
# using normal method
print(a[0]+a[1]+a[2]+a[3])
# using loop
i=0
sum=0
for i in range(0,len(a)):
    sum=sum+a[i]
    i=i+1
print(sum)