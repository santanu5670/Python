import mysql.connector
from mysql.connector import Error
class College_student:
    def __init__(self):
        try:
            self.connection=mysql.connector.connect(host="localhost",port='3307',database="python1",user="root",password="root")
            query='''create table if not exists college_student
            (Name varchar(10) not null,
            student_id integer primary key auto_increment,
            Age Integer check(age>17 && age<70) not null,
            Gender varchar(4) check(Gender in('Male','Female','Transgender')) not null,
            course_name varchar(10) check(course_name in('BCA','MCA','BTECH','MTECH','BSC','MSC','BBA','MBA')) not null,
            Duration integer check(Duration in(2,3,4)) not null,
            Entry_year integer check(Entry_year>1952 && Entry_year<2022),
            passout_year integer not null)'''
            mycoursor=self.connection.cursor()
            mycoursor.execute(query)
            print("Table Created")
        except Error as e:
            print(e)
    def insert_data(self,Name,Age,Gender,course_name,Duration,Entry_year,passout_year):
        try:
            query='''Insert into college_student(Name,Age,Gender,course_name,Duration,Entry_year,passout_year) values('{}',{},'{}','{}',{},{},{})'''.format(Name,Age,Gender,course_name,Duration,Entry_year,passout_year)
            print(query)
            mycoursor1=self.connection.cursor()
            mycoursor1.execute(query)
            print("Data are Saved to the Database")
            query1='''select student_id from college_student where name={}'''.format(Name)
            mycoursor1.execute(query1)
            for id in mycoursor1:
                print("Your Id is:",id)
            self.connection.commit()
        except Error as e:
            print(e)
    def update_Name(self,Name,student_id):
        query="update college_student set name='{}' where student_id={}".format(Name,student_id)
        print(query)
        mycursor2=self.connection.cursor()
        mycursor2.execute(query)
        print("Table Upadted")
        self.connection.commit()
    def update_Age(self,Age,student_id):
        query="update college_student set Age={} where student_id={}".format(Age,student_id)
        print(query)
        mycursor2=self.connection.cursor()
        mycursor2.execute(query)
        print("Table Upadted")
        self.connection.commit()
    def update_Gender(self,Gender,student_id):
        query="update college_student set Gender='{}' where student_id={}".format(Gender,student_id)
        print(query)
        mycursor2=self.connection.cursor()
        mycursor2.execute(query)
        print("Table Upadted")
        self.connection.commit()
    def update_course_name(self,course_name,student_id):
        query="update college_student set course_name='{}' where student_id={}".format(course_name,student_id)
        print(query)
        mycursor2=self.connection.cursor()
        mycursor2.execute(query)
        print("Table Upadted")
        self.connection.commit()
    def update_Duration(self,Duration,student_id):
        query="update college_student set Duration={} where student_id={}".format(Duration,student_id)
        print(query)
        mycursor2=self.connection.cursor()
        mycursor2.execute(query)
        print("Table Upadted")
        self.connection.commit()
    def update_Entry_year(self,Entry_year,student_id):
        query="update college_student set Entry_year={} where student_id={}".format(Entry_year,student_id)
        print(query)
        mycursor2=self.connection.cursor()
        mycursor2.execute(query)
        print("Table Upadted")
        self.connection.commit()
    def update_passout_year(self,passout_year,student_id):
        query="update college_student set passout_year={} where student_id={}".format(passout_year,student_id)
        print(query)
        mycursor2=self.connection.cursor()
        mycursor2.execute(query)
        print("Table Upadted")
        self.connection.commit()
    def show_profile(self,id):
        query="select * from college_student where student_id={}".format(student_id)
        mycursor3=self.connection.cursor()
        mycursor3.execute(query)
        for s in mycursor3:
            print("Name: ",s[0])
            print("Student Id: ",s[1])
            print("Age: ",s[2])
            print("Gender: ",s[3])
            print("Course Name: ",s[4])
            print("Duration: ",s[5])
            print("Admission Year: ",s[6])
            print("Passout Year: ",s[7])
    def delete(self,student_id):
        query="delete from college_student where student_id={}".format(student_id)
        print(query)
        mycorsor3=self.connection.cursor()
        mycorsor3.execute(query)
        self.connection.commit()
        print("Data Deleted")
db=College_student()
ch=int(input('''Choose the below option
1.Student Entry
2.Update Details
3.Show Profile
4.Delete Profile
'''))
if ch==1:
    Name=input("Enter Your Name\n")
    # student_id=int(input("Enter Your Id\n"))
    Age=int(input("Enter Your Age\n"))
    Gender=input("Enter Your Gender\n")
    Course_name=input("Enter Your Course Name\n")
    Duration=int(input("Enter Course Duration\n"))
    Admission_year=int(input("Enter Your Admission Year\n"))
    passout_year=int(input("Enter Your Passout Year\n"))
    db.insert_data(Name,Age, Gender, Course_name, Duration, Admission_year, passout_year)
elif ch==2:
    option=int(input('''Choose What do you want to update
    1. Name
    2. Age
    3. Gender
    4.Course Name
    5.Duration
    6.Admission Year
    7.Passout Year \n'''))
    if option==1:
        Name=input("Enter Your Name\n")
        student_id=int(input("Enter Your Id\n"))
        db.update_Name(Name,student_id)
    elif option==2:
        Age=int(input("Enter Your Age\n"))
        student_id=int(input("Enter Your Id\n"))
        db.update_Age(Age,student_id)
    elif option==3:
        Gender=input("Enter Your Gender\n")
        student_id=int(input("Enter Your Id\n"))
        db.update_Gender(Gender,student_id)
    elif option==4:
        Course_name=input("Enter Your Course Name\n")
        student_id=int(input("Enter Your Id\n"))
        db.update_course_name(Course_name,student_id)
    elif option==5:
        Duration=int(input("Enter Your Age\n"))
        student_id=int(input("Enter Your Id\n"))
        db.update_Duration(Duration,student_id)
    elif option==6:
        Admission_year=int(input("Enter Your Admission Year\n"))
        student_id=int(input("Enter Your Id\n"))
        db.update_Entry_year(Admission_year,student_id)
    elif option==7:
        passout_year=int(input("Enter Your Age\n"))
        student_id=int(input("Enter Your Id\n"))
        db.update_passout_year(passout_year,student_id)
    else:
        print("Wrong Choice")
elif ch==3:
    student_id=int(input("Enter Your ID\n"))
    db.show_profile(student_id)
elif ch==4:
    student_id=int(input("Enter Your Id\n"))
    db.delete(student_id)
else:
    print("Not Available")






