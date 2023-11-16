r = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
ans = [0] * 40
a = int(input())
b = int(input())
n = int(input())
for _ in range(n):
    r.append(int(input()))

r.sort()
ans[0] = 1
for i in range(1, 14 + n):
    for j in range(i):
        if a <= r[i] - r[j] <= b:
            ans[i] += ans[j]

print(ans[13 + n])
