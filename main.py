import mysql.connector
from tabulate import tabulate
from datetime import date

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=<password>
)

mycursor = mydb.cursor()
today = date.today()
d1=today.strftime("%Y/%m/%d")

def database_creation():
    database_create = "CREATE DATABASE IF NOT EXISTS student"
    mycursor.execute(database_create)
    mycursor.execute("use student")
    stu_data_sql = '''
                    CREATE TABLE IF NOT EXISTS student_data
                    (sid integer primary key AUTO_INCREMENT,
                    name char(25),
                    dob date,
                    phone char(10),
                    city char(20),
                    class integer)
                    '''
    stu_marks_sql = '''
                    CREATE TABLE IF NOT EXISTS student_marks
                    (tid integer primary key AUTO_INCREMENT,
                    sid integer,
                    pyear integer,
                    class integer,
                    sroll integer,
                    tmarks integer)
                    '''
    stu_fees_sql = '''
                    CREATE TABLE IF NOT EXISTS fees
                    (txid integer primary key AUTO_INCREMENT,
                    sid integer,
                    amount integer,
                    pay_date date,
                    MoP char(10))
                    '''
    mycursor.execute(stu_data_sql)
    mycursor.execute(stu_marks_sql)
    mycursor.execute(stu_fees_sql)

def student_data():
    mycursor.execute("SELECT * FROM student_data ORDER BY sid")
    my_result = mycursor.fetchall()
    return my_result

def student_marks():
    mycursor.execute("SELECT * FROM student_marks ORDER BY tid")
    my_result = mycursor.fetchall()
    return my_result

def student_fees():
    mycursor.execute("SELECT * FROM fees ORDER BY txid")
    my_result = mycursor.fetchall()
    return my_result

def add_student():
    name = input("enter the student name :- ")
    dob = input("enter the date of birth (yyyy/mm/dd) :- ")
    no = input("enter the student number")
    city = input("enter the student city")
    clas = input("enter the student class")
    val = (name ,dob ,no ,city ,clas)
    add_stu_sql = "INSERT INTO student_data (name, dob, phone, city, class) VALUES (%s,%s,%s,%s,%s)"
    mycursor.execute(add_stu_sql, val)
    mydb.commit()

def add_student_marks():
    sid = input("enter the student ID :- ")
    pyear = input("enter the passing Year :- ")
    sroll = input("enter the student Roll number")
    tmarks = input("enter the student tmarks")
    clas = input("enter the student class")
    val = (sid ,pyear ,clas ,sroll ,tmarks)
    add_marks_sql = "INSERT INTO student_marks (sid ,pyear ,class ,sroll ,tmarks) VALUES (%s,%s,%s,%s,%s)"
    mycursor.execute(add_marks_sql, val)
    mydb.commit()

def add_fees():
    sid = input("enter the student ID :- ")
    amount = input("enter the amount :- ")
    MoP = input("enter the mode of payment :- ")
    val = (sid, amount, d1, MoP)
    add_stu_sql = "INSERT INTO fees (sid, amount, pay_date, MoP) VALUES (%s,%s,%s,%s)"
    mycursor.execute(add_stu_sql, val)
    mydb.commit()

database_creation()

while True:
    data=[]
    print()
    print("1.show student details \n"+"2.to add student \n"+"3.show student marks \n"+"4.give student marks \n"+"5.show fees details \n"+"6.to take fees \n"+"7.to exit \n")
    n = int(input("enter your choice :- "))
    
    if n == 1:
        myresult = student_data()
        for x in myresult:
            data.append(x)
        table = tabulate(data, headers=["ID", "Name", "Date of birth", "Number", "City", "Class"])
        print(table)        
    elif n == 2:
        add_student()
    elif n == 3:
        myresult = student_marks()
        for x in myresult:
            data.append(x)
        table = tabulate(data, headers=["Marks ID", "Student ID", "Passing year", "Class", "Roll no.", "Total marks"])
        print(table)    
    elif n == 4:
        add_student_marks()
    elif n == 5:
        myresult = student_fees()
        for x in myresult:
            data.append(x)
        table = tabulate(data, headers=["Payment ID", "Student ID", "Amount", "Payment Date", "Mode of payment"])
        print(table)    
    elif n == 6:
        add_fees()
    elif n == 7:
        break
    else:
        print("enter a valid number")
