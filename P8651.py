def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    return False


def year(y, m, d):
    ans_tmp = ''
    if int(y) > 60:
        ans_tmp += '19' + y
    else:
        ans_tmp += '20' + y
    if is_leap_year(int(ans_tmp)) and 0 < int(m) <= 12:
        if leap_year[int(m)] >= int(d) > 0:
            return ans_tmp + '-%s-%s' % (m, d)
    elif not is_leap_year(int(ans_tmp)) and 0 < int(m) <= 12:
        if ordinary_year[int(m)] >= int(d) > 0:
            return ans_tmp + '-%s-%s' % (m, d)


def bubble_sort(li):
    for i in range(0, len(li) - 1):
        for j in range(0, len(li) - i - 1):
            if li[j][0:4] == li[j + 1][0:4] and int(li[j][5:7]) > int(li[j + 1][5:7]):
                li[j], li[j + 1] = li[j + 1], li[j]
            if li[j][0:7] == li[j + 1][0:7] and int(li[j][8:]) >= int(li[j + 1][8:]):
                li[j], li[j + 1] = li[j + 1], li[j]


leap_year = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ordinary_year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

AA, BB, CC = input().strip().split('/')
ans = []
tmp = [year(AA, BB, CC), year(CC, AA, BB), year(CC, BB, AA)]
for i in tmp:
    if i is not None:
        ans.append(i)
ans = list(set(ans))
ans.sort(key=lambda x: x[0:4])
bubble_sort(ans)
for i in ans:
    print(i)
