# f=open('E:\Python(6th sem)\coding\9\sample.txt','r')
f=open('E:\Python(6th sem)\coding\9\sample.txt') #if you don't specify any mode by default mood is r
data=f.read()
# data1=f.read(5) #it read only 5 character from the file
print(data)
# print(data1)
f.close()