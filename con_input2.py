fname=input("Enter first name:")
lname=input("Enter last name:")
phone=input("Enter phone number:")
age=input("Enter age:")
city=input("Enter city:")
sal=input("Enter salary:")
dept=input("Enter department name:")

while ((fname=="" or fname.isalpha()==False) or (lname=="" or lname.isalpha()==False) or 
       (len(phone)!=10 or phone.isnumeric()==False) or (int(age)<=20 or age.isnumeric()==False or len(age)>3 or len(age)<2) 
       or (city=="" or city.isalpha()==False) or (int(sal)<0 or sal=="") or (dept=="" or dept.isalpha()==False)):
    if fname=="" or fname.isalpha()==False:
        print("Enter valid first name.")
        fname=input("Re-enter first name:")
        
    if lname=="" or lname.isalpha()==False:
        print("Enter valid last name.")
        lname=input("Re-enter last name:")
    
    if len(phone)!=10 or phone.isnumeric()==False:
        print("Enter valid phone number.")
        phone=input("Re-enter phone number:")
        
    if int(age)<=20 or age.isnumeric()==False or len(age)<2 or len(age)>3:
        print("Enter valid age.")
        age=input("Re-enter valid age")
    
    if city=="" or city.isalpha()==False:
        print("Enter valid city name.")
        city=input("Re-enter city name")
        
    if (int(sal)<0 or sal==""):
        print("Enter valid salary.")
        sal=input("Re-enter salary")
        
    if (dept=="" or dept.isalpha()==False):
        print("Enter valid department name.")
        dept=input("Re-enter department name")
        
print("Name:",fname,lname)
print("Phone:",phone)
print("Age:",age)
print("City:",city)
print("Salary:",sal)
print("Department:",dept)