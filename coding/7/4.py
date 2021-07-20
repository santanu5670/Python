n = int(input("Enter a number = "))
i=0
flag=1
for i in range(2,n//2):
    if(n%i==0):
        flag=0
        break
    else:
        flag=1
        break
if flag==1:
    print("The number is prime")
else:
    print("The number is not prime")