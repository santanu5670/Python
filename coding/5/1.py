mydict={
    "Pankha":"Fan",
    "Dubba": "Box",
    "kalam":"Pen",
    "Chatra":"Student"
}
print("Options are",mydict.keys())
a=input("Enter the word what you want to search \n")
# print("The meaning of",a,"is = ",mydict[a])
f = mydict.get(a)
# if (f is None):
#     print("Sorry The Word is not available into our Dectionary")
# else:
#     print("The meaning of",a,"is = ",f)

if f == None:
    print("Sorry The Word is not available into our Dectionary")
else:
    print("The meaning of",a,"is = ",f)
    

