f=open('E:\Python(6th sem)\coding\9\sample.txt')
print(f.tell()) #it is used to tell where our file pointer is present
print(f.readline())
print(f.tell())
print(f.readline())

f.seek(10)
print(f.readline())

f.seek(0) 
'''it is used to restart the pointer at specific location like 0,10 etc then if we want to print it will start 
 at print at this position'''
print(f.readline())
f.close()


