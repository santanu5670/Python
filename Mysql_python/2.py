import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port=3307,
  user="root",
  password="root",
  database="python1"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")