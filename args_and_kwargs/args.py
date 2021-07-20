# def function1(a,b,c,d,e):
#     print(a,b,c,d,e)
# function1("Dev","Rohon","Ramesh","Rahul","Harsh")
'''Using *args'''
def function1(*args):
    print(type(args)) #in args element are stored in a tuple
    for i in args:
        print(i)
def function2(normal,*names): #we can put other name instead of *args
    print(normal,"and the name of the students are=")
    for item in names:
        print(item)
lst=["Dev","Rohon","Ramesh","Rahul","Harsh"]
function1(*lst)
function2("I am a normal people","Dev","Rohon","Ramesh","Rahul","Harsh")
function2("I am a normal people") 
