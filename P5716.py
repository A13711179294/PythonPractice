def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


y, m = map(int, input().split())
if m == 1:
    print(31)
if m == 2:
    if is_leap_year(y):
        print(29)
    else:
        print(28)
if m == 3:
    print(31)
if m == 4:
    print(30)
if m == 5:
    print(31)
if m == 6:
    print(30)
if m == 7:
    print(31)
if m == 8:
    print(31)
if m == 9:
    print(30)
if m == 10:
    print(31)
if m == 11:
    print(30)
if m == 12:
    print(31)

