import bisect

n = int(input())
a = input().split()
b = []
for i in range(0, 2 * n, 2):
    b.append([int(a[i]), int(a[i + 1])])

b.sort(key=lambda x: (x[0], x[1]), reverse=True)

ans = [b[0][1]]
len1 = 1
for i in range(1, n):
    if b[i][1] > ans[len1 - 1]:
        ans.append(b[i][1])
        len1 += 1
    else:
        k = bisect.bisect_left(ans, b[i][1])  # 二分
        ans[k] = b[i][1]

print(len1)
