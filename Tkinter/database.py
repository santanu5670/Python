import test_database_tkinter as tdt
import mysql.connector
def data_insert():
    connection=mysql.connector.connect(host='localhost',port='3307',database='python1',user='root',password='root')
    query="create table if not exists Travel(namevalues varchar(10),phonevalues varchar(10), gendervalues varchar(4),emergencyvalues varchar(10),paymentvalues varchar(10),foodservicevalues Integer(10))"
    mycursor=connection.cursor()
    mycursor.execute(query)

    query1="insert into Travel values('{}','{}','{}','{}','{}',{})".format(tdt.namevalues.get(),tdt.phonevalues.get(),tdt.gendervalues.get(),tdt.emergencyvalues.get(),tdt.paymentvalues.get(),tdt.foodservicevalues.get())
    mycursor1=connection.cursor()
    mycursor1.execute(query1)
    connection.commit()