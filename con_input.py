x=int(input("Enter salary:"))
y=input("Enter name:")
z=input("Enter department:")
p=input("Enter phone number:")
while y=="" or z=="" or x<=0 or len(p)!=10:
    if y =="":
        print("Name cannot be null. Re-enter name")
        y=input("Enter name:")
    if z =="":
        print("Department cannot be null. Re-enter department")
        z=input("Enter department:")
    if x <=0:
        print("Salary cannot be less than 0. Re-enter value")
        x=int(input("Enter salary:"))
    if len(p)!=10:
        print("Enter a valid 10 digit phone number")
        p=input("Enter phone number:")

print("Name:",y)
print("Department:",z)
print("Salary:",x)
print("Phone Number:",p)