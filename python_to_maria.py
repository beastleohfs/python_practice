import mariadb
import sys
conn=mariadb.connect(
    user="root",
    password="1234",
    host="localhost",
    port=3306,
    database="employees")

curr=conn.cursor()
conn.autocommit=True

try:
    curr.execute("CREATE TABLE new_stud (id INTEGER PRIMARY KEY,fname VARCHAR(30), lname VARCHAR(30),age INTEGER,gender CHAR,city VARCHAR(255),dept VARCHAR(255),salary INTEGER)");

except Exception as y:
    print(y)

def check_id():
    id1=input("Enter id:")
    while id1.isnumeric()==False:
        print("Enter valid id.")
        id1=input("Re-enter valid id:")
    return int(id1)

def check_fname():
    fname=input("Enter first name:")
    while fname=="" or fname.isalpha()==False:
        print("Enter valid first name.")
        fname=input("Re-enter first name:")
    return fname

def check_lname():
    lname=input("Enter last name:")
    while lname=="" or lname.isalpha()==False:
        print("Enter valid last name.")
        fname=input("Re-enter last name:")
    return lname

def check_phone():
    phone=input("Enter phone number:")
    while len(phone)!=10 or phone.isnumeric()==False:
        print("Enter valid phone number.")
        phone=input("Re-enter phone number:")
    return phone

def check_gender():
    gender=input("Enter Gender:")
    while gender.upper()!='M' and gender.upper()!='F':
        print("Enter valid gender. I support LGBTQ")
        gender=input("Re-enter gender:")
    return gender

def check_age():
    age=input("Enter valid age")
    while int(age)<=20 or age.isnumeric()==False or len(age)<2 or len(age)>3:
        print("Enter valid age.")
        age=input("Re-enter valid age")
    return int(age)

def check_city():
    city=input("Enter city name")
    while city=="" or city.isalpha()==False:
        print("Enter valid city name.")
        city=input("Re-enter city name")
    return city

def check_sal():
    sal=input("Enter salary")
    while (int(sal)<0 or sal==""):
        print("Enter valid salary.")
        sal=input("Re-enter salary")
    return int(sal)

def check_dept():
    dept=input("Enter department name")
    while (dept=="" or dept.isalpha()==False):
        print("Enter valid department name.")
        dept=input("Re-enter department name")
    return dept

limit=int(input("enter number of entries:"))
for _ in range(limit):
    query="""INSERT INTO new_stud (id,fname,lname,age,gender,city,dept,salary) VALUES (%d,%s,%s,%d,%s,%s,%s,%d)"""
    record=(check_id(),check_fname(),check_lname(),check_age(),check_gender(),check_city(),check_dept(),check_sal())
    curr.execute(query,record)

curr.execute("select * from new_stud;")
for (id1,fname,lname,age,gender,city,dept,salary) in curr :
    print("id:",id1,"| Name:",fname,lname,"| Age:",age,"| Gender:",gender,"| City:",city,"| Salary:",salary,"| Department:",dept)