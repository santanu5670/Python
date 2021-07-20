n = int(input("Enter a number = "))
i=0
Prime=True
for i in range(2,n//2):
    if(n%i==0):
        Prime=False
        break
if Prime:
    print("The number is prime")
else:
    print("The number is not prime")