import mysql.connector
class Database_college:
    #Create table
    def __init__(self):
        self.connection=mysql.connector.connect(host='localhost',port='3307',database='python1',user='root',password='root')
        query="create table if not exists college(name varchar(10),student_id Integer(10),course_name varchar(10))"
        mycursor=self.connection.cursor()
        mycursor.execute(query)
        print("Table Created")
    #Insert Data
    def insert(self,name,student_id,course_name):
        query="insert into college values('{}',{},'{}')".format(name,student_id,course_name)
        print(query)
        mycursor1=self.connection.cursor()
        mycursor1.execute(query)
        print("Data Saved into database")
        self.connection.commit()
    def upadte(self,name,student_id):
        query="update college set name='{}' where student_id={}".format(name,student_id)
        print(query)
        mycursor2=self.connection.cursor()
        mycursor2.execute(query)
        print("Table Upadted")
        self.connection.commit()
    def display(self):
        query="select * from college"
        print(query)
        mycursor3=self.connection.cursor()
        mycursor3.execute(query)
        print("Table Upadted")
        for db in mycursor3:
            print("Name:",db[0])
            print("Id:",db[1])
            print("Course_name:",db[2])
        self.connection.commit()
    def delete(self,student_id):
        query="delete from college where student_id={}".format(student_id)
        print(query)
        mycorsor4=self.connection.cursor()
        mycorsor4.execute(query)
        print("Data Deleted")
db=Database_college()
db.insert("Satyajit",2,"BCA")
db.delete(2)
db.display()
db.insert("Satyajit",2,"BCA")
db.upadte('Soujatya',2)
db.display()
