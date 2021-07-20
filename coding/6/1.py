num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
num3 = int(input("Enter third number = "))
num4 = int(input("Enter fourth number = "))

# if num1>num2 and num1>num3 and num1>num4:
#     print(num1,"is greatest")
# elif num2>num1 and num2>num3 and num2>num4:
#     print(num2,"is greatest")
# elif num3>num1 and num3>num2 and num3>num4:
#     print(num3,"is greatest")
# else:
#     print(num4,"is greatest")

if (num1>num4):
    # pass 
    # The pass statement is used as a placeholder for future code. When the pass statement is executed, 
    # nothing happens, but you avoid getting an error when empty code is not allowed. Empty code is not allowed
    #  in loops, function definitions, class definitions, or in if statements.
    f1=num1
else:
    f1=num4

if (num2>num3):
    f2=num2
else:
    f2=num3
if f1>f2:
    print(str(f1)+"is greatest")
else:
    print(str(f2)+"is greatest")


