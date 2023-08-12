n, q = map(int, input().split())
a = [0] * (n + 1)
dic = {}
for _ in range(q):
    tmp = list(map(int, input().split()))
    if len(tmp) == 4:
        i = tmp[1]
        j = tmp[2]
        k = tmp[3]
        dic[(i, j)] = k
    else:
        i = tmp[1]
        j = tmp[2]
        print(dic[(i, j)])
