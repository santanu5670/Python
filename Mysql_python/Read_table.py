import mysql.connector
from mysql.connector import Error
try:
    connection=mysql.connector.connect(host='localhost',port='3307',database='python1',user='root',password='root')
    mycursor=connection.cursor()
    # mycursor.execute("select name from course")
    # myresult=mycursor.fetchone()
    mycursor.execute("select * from course")
    myresult=mycursor.fetchall()
    for row  in myresult:
        print(row)
except Error as e:
    print(e)