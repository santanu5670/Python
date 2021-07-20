for i in range(10):
    print(i)
    if i==5:
        break
# Here else part is not executed because else part only executed when for loop executed completely but due 
# to the reason of break it not executed properly
else:
    print("This is under the else part")  #it is executed properly when loop is successfully executed