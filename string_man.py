fname=input("Enter first name:")
lname=input("Enter last name:")
gender=input("enter m for male and f for female:")
age=int(input("Enter age:"))
dob=input("Enter date of birth:")
mobile=int(input("Enter mobile number:"))
country=input("enter country name:")
city=input("enter city name:")
pincode=int(input("enter pin code:"))
house_add=input("enter house number:")
street=input("enter street name")
print("Name:",fname,lname,"/",gender,sep=" ")
print("Date of birth:",dob,"/",age)
print("Phone Number:",mobile)
print("Address:",str(house_add),street,city,country,sep=",",end="-")
print(pincode)