def swap(x, y):
    a[x], a[y] = a[y], a[x]


n = int(input())
a = [0]
a.extend(list(map(int, input().split())))
ans = 0
for i in range(1, n + 1):
    if a[i] != i:
        for j in range(i + 1, n + 1):
            if a[j] == i:
                swap(i, j)
                ans += 1
                break

print(ans)

