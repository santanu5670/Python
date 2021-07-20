import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port=3307,
  user="root",
  password="root",
  database="python1"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")