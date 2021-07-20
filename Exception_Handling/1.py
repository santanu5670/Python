try:
    f=open('Sample.txt')
except:
    print("File not found")
else:
    print("File Opened Successfully") #Use else block if exception not occure