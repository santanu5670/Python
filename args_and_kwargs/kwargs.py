def function1(normal,*args,**kwargs): #we can put other name instead of *args
    print(normal)
    for item in args:
        print(item)
    print("Now I would introduce professions of them")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
# def function2(*args):
#     for key, value in args.items():
#         print(f"{key} is a {value}")
lst=["Dev","Rohon","Ramesh","Rahul","Harsh"]
kw={"Dev":"Monitor","Rohon":"Instructor","Ramesh":"Professor","Rahul":"Programmer","Harsh":"Developer"}
function1("I am a normal people",*lst,**kw)
print("************************************************************")
function1(*lst,**kw) #if we not want to put the value of normal we also can do that
# print("************************************************************")
# function2(kw)
''' We can not chage the order of parameter of the function means we cannot write 
def function1(*args,normal,**kwargs) we always have to maintain the order def function1(normal,*args,**kwargs)'''