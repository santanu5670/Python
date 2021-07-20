n=int(input("Enter a number"))
def factorial_recursion(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial_recursion(n-1)
# def factorial(number):
#     fact=1
#     for i in range(1,number+1):
#         fact=fact*i
#     print(fact)
# factorial()
f=factorial_recursion(n)
print(f)



    
