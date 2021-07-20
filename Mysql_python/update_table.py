import mysql.connector
from mysql.connector import Error
try:
    connection=mysql.connector.connect(host='localhost',port='3307',database='python1',user='root',password='root')
    mycursor=connection.cursor()
    sql="UPDATE course set name='python' where id=0"
    mycursor.execute(sql)
    connection.commit()
except Error as e:
    print(e)
