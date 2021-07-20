import mysql.connector
from mysql.connector import Error
connection=mysql.connector.connect(host='localhost',port='3307',database='python1',user='root',password='root')
mycursor=connection.cursor()
mycursor.execute("create table course(name varchar(10),id INTEGER,address varchar(21))")