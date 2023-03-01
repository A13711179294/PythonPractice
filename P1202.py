def is_leap_year(x):
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        return True
    else:
        return False


def mouth_day(x, flag):
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
        return 31
    elif x == 2:
        if flag:
            return 29
        else:
            return 28
    else:
        return 30


n = int(input())
dict1 = {}
days = 1
for i in range(1900, 1900 + n):
    flag = is_leap_year(i)
    for j in range(1, 13):
        for k in range(1, mouth_day(j, flag) + 1):
            if k == 13:
                dict1[days] = dict1.get(days, 0) + 1
            days += 1
            if days == 8:
                days = 1

print(dict1[6], dict1[7], dict1[1], dict1[2], dict1[3], dict1[4], dict1[5])
