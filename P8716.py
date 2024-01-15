def leap_year(x):
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        return True
    return False


days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

n = input()
year = int(n[0:4])
month = int(n[4:6])
day = int(n[6:8])

flag1 = 0
ans1 = ''
ans2 = ''

for i in range(year, 9221):
    cnt = ''
    tmp = list(reversed(str(i)))
    if leap_year(i):
        flag1 = 1

    if int(tmp[0] + tmp[1]) <= 12:
        if flag1 == 1 and int(tmp[0] + tmp[1]) == 2:
            if int(tmp[2] + tmp[3]) <= 29:
                cnt += str(i) + ''.join(tmp)
        elif int(tmp[2] + tmp[3]) <= days[int(tmp[0] + tmp[1])]:
            cnt += str(i) + ''.join(tmp)

        if cnt == n:
            continue

        if ans1 == '':
            ans1 = cnt
        if len(set(cnt)) == 2 and cnt[0] == cnt[2] and cnt[1] == cnt[3]:
            ans2 = cnt
            break

print(ans1)
print(ans2)
