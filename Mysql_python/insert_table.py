import mysql.connector
from mysql.connector import Error
try:
    connection=mysql.connector.connect(host='localhost',port='3307',database='python1',user='root',password='root')
    mycursor=connection.cursor()
    sqlfrom="insert into course values(%s,%s,%s)"
    courses=[("P_basic",0,"AB"),("J_basic",1,"BD")]
    mycursor.executemany(sqlfrom, courses)
    connection.commit()
except Error as e:
    print(e)