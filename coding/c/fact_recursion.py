def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        f=n*factorial(n-1)
        return f
n=int(input("Enter a number = "))
x=factorial(n)
print(x)
