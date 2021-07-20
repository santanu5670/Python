username = input("Enter use name = ")
if len(username)<10:
    print("It contain less than 10 characters")
elif len(username) is 10:
    print("It contain exactly 10 character")
else:
    print("It contain grater that 10 character")