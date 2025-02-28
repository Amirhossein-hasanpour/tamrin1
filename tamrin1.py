def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
        return True
    else:
        return False
year = int(input("سال: "))
if is_leap_year(year):
    print(f"{year} کبیسه هست: ")
else:
    print(f"{year} کبیسه نیست ")