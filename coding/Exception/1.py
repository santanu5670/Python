try:
    a=int(input("Enter first number="))
    b=int(input("Enter second number="))
    print("The addition is",
        a+b)
except Exception as e:
    print(e)
print("This is a Exception handling program")
