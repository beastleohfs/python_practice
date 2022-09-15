

def hra(bs):
    hra=50/100*bs
    return int(hra)

def da(bs):
    da=30/100*bs
    return int(da)

def bonus(bs):
    bonus=(bs)*(10/100)
    return int(bonus)

def salary(bs):
    sal=bs+bonus(bs)
    return int(sal)