import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='nsec',password='nsec',database='mysql')
print(mydb)
if(mydb):
    print('Connection successful')
else:
    print('Connection Unsuccessful')