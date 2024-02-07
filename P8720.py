def node(a, b, c, d):
    x = (d - b) / (a - c)
    y = a * x + b
    return x, y


N = int(input())
number = []
tmp = N
while tmp > 0:
    number.append(tuple(map(int, input().split())))
    tmp -= 1

s1 = list(set(number))
l1 = len(s1)

ans = 1
for i in range(l1):
    s2 = set()
    for j in range(i + 1, l1):
        if s1[i][0] != s1[j][0]:
            ret1, ret2 = node(s1[i][0], s1[i][1], s1[j][0], s1[j][1])
            if (ret1, ret2) not in s2:
                s2.add((ret1, ret2))
    ans += len(s2) + 1

print(ans)
