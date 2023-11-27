def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


begin, end = map(int, input().split())
a = []
for i in range(begin, end + 1):
    if is_leap_year(i):
        a.append(i)

print(len(a))
for i in a:
    print(i, end=' ')
