k = int(input().strip())
s = input().strip()
l = len(s) / k

if l == int(l):
    l = int(l)
    str1 = []
    for i in range(0, len(s), l):
        tmp = ''
        for j in range(i, i + l):
            tmp += s[j]
        str1.append(tmp)

    ans = 0
    for j in range(0, l):
        tmp_dict = {}
        for i in range(0, len(str1)):
            tmp_dict[str1[i][j]] = tmp_dict.get(str1[i][j], 0) + 1
        if len(tmp_dict) == 1:
            pass
        else:
            tmp_dict.pop(max(tmp_dict, key=tmp_dict.get))
            for k in tmp_dict.values():
                ans += k

    print(ans)
else:
    print(-1)
