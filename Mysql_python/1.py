import mysql.connector
from mysql.connector import Error
try:
    connection=mysql.connector.connect(host='localhost',port='3307',database='office',user='root',password='root')
    if connection.is_connected():
        db_info=connection.get_server_info()
        print("Connected to the mysql server version:",db_info)
        cursor=connection.cursor()
        cursor.execute("Select Database();")
        record=cursor.fetchone()
        print("You are connected to the database",record)
except Error as e:
    print("Error while connecting to the databases",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection is closed")


# import mysql.connector
# from mysql.connector import Error
# try:
#     mydb = mysql.connector.connect(
#     host="localhost",
#     port="3307",
#     user="root",
#     password="root"
#     )
#     print(mydb)
# except Error as e:
#     print(e)

