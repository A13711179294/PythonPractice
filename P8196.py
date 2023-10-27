t = int(input())
tmp = t
while tmp > 0:
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(0, n):
        for j in range(i, n):
            for k in range(j, n):
                if a[i] + a[j] == a[k]:
                    ans += 1
    print(ans)
    tmp -= 1