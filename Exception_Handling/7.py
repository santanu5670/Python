#create our own exception class from Exception main class
class ValueSmallError(Exception):
    def __str__(self):
        return("Value is too small")
class ValueBigError(Exception):
    def __str__(self):
        return("Value is too big")
number=10
while True:
    try:
        num=int(input("Enter a number"))
        if num<number:
            raise ValueSmallError
        elif num>number:
            raise ValueBigError
        break
    except ValueSmallError as e:
        print(e)
        print()
    except ValueBigError:
        print("The is too big")
        print()
print("Congratulation!you guess it Correctly")

