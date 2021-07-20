# f=open('E:\Python(6th sem)\coding\9\sample.txt','r')
f=open('E:\Python(6th sem)\coding\9\sample.txt','rt') 
# rt and r are samre if we write r then bydefault t is placed with r 
# data=f.readline() #for printing first linr
# print(data)
# data=f.readline() #for printing second line
# print(data)
data1=f.readlines() #it is used to print lines in a list
print(data1)
f.close()