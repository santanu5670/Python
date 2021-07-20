try:
    f=open('Sample1.txt')
# except Exception:  #Exception is a class which store all type of exception
#     print("File not found")
except FileNotFoundError: 
    #we can also put here FilenotFoundError instead of Exception but if we not know what type of error it is 
    # then simply put Exception class
    print("File not found")
else:
    s=f.readline()
    print(s)
    f.close()