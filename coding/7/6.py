n=int(input("Enter a number"))
fact=1
if n>=0:
    for i in range(1,n+1):
        fact=fact*i
        i=i+1
    print(f"Tha Factorial of {n} is {fact}")
else:
    print(f"Factorial of {n} is not possible")