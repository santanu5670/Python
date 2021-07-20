a=int(input("Enter First Number"))
b=int(input("Enter second Number"))
c=int(input("Enter third Number"))
def greatest():
    """This is a function to find the greatest between three numbers"""
    #This process is called docstring which tell the defination of function
    if a>b and a>c:
        print(a,"is largest")
    elif b>a and b>c:
        print(b,"is largest")
    else:
        print(c,"is largest")
greatest()
print(greatest.__doc__) #This process is called docstring which tell the defination of function


