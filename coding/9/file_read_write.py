f=open('E:\Python(6th sem)\coding\9\sample.txt','r+')
# If we eant to perform read or write operation simultaniously
data=f.read()
print(data)
data1=f.write("Thank You")
print(data1)
