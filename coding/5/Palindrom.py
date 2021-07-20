n = int(input("Enter a number \n "))
q  = n
rev = 0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if q==rev:
    print("The number",q,"is Palindrom")
else:
    print("The number",q,"is not Palindrom")
