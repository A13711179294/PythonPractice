tiangan = {1: 'jia', 2: 'yi', 3: 'bing', 4: 'ding', 5: 'wu', 6: 'ji', 7: 'geng', 8: 'xin', 9: 'ren', 10: 'gui'}
dizhi = {1: 'zi', 2: 'chou', 3: 'yin', 4: 'mao', 5: 'chen', 6: 'si', 7: 'wu', 8: 'wei', 9: 'shen', 10: 'you', 11: 'xu',
         12: 'hai'}
year = int(input())
flag = 2020
i = 7
j = 1
if year >= 2020:
    for _ in range(2020, year):
        i += 1
        j += 1
        if i == 11:
            i = 1
        if j == 13:
            j = 1
else:
    for _ in range(2020, year, -1):
        i -= 1
        j -= 1
        if i == 0:
            i = 10
        if j == 0:
            j = 12


print(tiangan[i] + dizhi[j])
