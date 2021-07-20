import mysql.connector
from mysql.connector import Error
connection=mysql.connector.connect(host='localhost',port='3307',user='root',password='root')
mycursor=connection.cursor()
mycursor.execute("show databases")
for db in mycursor:
    print(db)
