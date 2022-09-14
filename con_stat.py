name=input("enter name:")
year=int(input("enter year of service"))
sal=int(input("enter salary"))
bonus=0
if year>=10:
    bonus=int(15*sal/100)
if year>=5:
    bonus=int(10*sal/100)
if year>=3:
    bonus=int(5*sal/100)
else:
    bonus=0
if bonus!=0:
    print("bonus:",bonus)
    print("total:",sal+bonus)
else:
    print("not eligible")