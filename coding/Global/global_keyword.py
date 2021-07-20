l=10 
m=20 
def function1():
    global l #global keyword gives us permission to change the value of global variable inside the function 
    l=l+45
    n=10 
    print(l,m,n) 
function1()
print(l,m)