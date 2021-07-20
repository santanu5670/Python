l=10 # Global variables means anyone can use this
m=20 # Global variables means anyone can use this
def function1():
    l=5 #local varialbe means only this function can use this
    n=10 #local varialbe means only this function can use this
    print(l,m,n) 
    '''here l is 5 so it can not take the value of global variable it but here m is not defined in this 
    function so it take the value of global variable'''
function1()
print(l,m)