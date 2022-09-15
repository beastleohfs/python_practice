import cal
fname = input("Enter your first name:")
lname = input("Enter last name:")
bs=int(input("Enter Basic Salary:"))
print("Name:",fname,lname,"\nHRA:",cal.hra(bs),"\nTotal Salary:",cal.salary(bs))