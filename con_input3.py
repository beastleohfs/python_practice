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

def check_age():
    age=input("Enter valid age")
    while int(age)<=20 or age.isnumeric()==False or len(age)<2 or len(age)>3:
        print("Enter valid age.")
        age=input("Re-enter valid age")
    return age

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
    return sal

def check_dept():
    dept=input("Enter department name")
    while (dept=="" or dept.isalpha()==False):
        print("Enter valid department name.")
        dept=input("Re-enter department name")
    return dept

print("Name:",check_fname(),check_lname(),"\nAge:",check_age(),"\nPhone Number:",check_phone(),"\nCity:",check_city(),"\nSalary:",check_sal(),"\nDepartment:",check_dept())
#print("Age:",check_age())
#print("Phone Number:",check_phone())
#print("City:",check_city())
#print("Salary:",check_sal())
#print("Department:",check_dept())