n = int(input())
a = [0] + list(map(int, input().split()))
s = [0]
for i in range(1, n + 1):
    s.append(s[i - 1] + a[i])

m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    print(s[r] - s[l - 1])
