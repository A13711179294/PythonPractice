n, k = map(int, input().split())
tmp = n
ans = 0
cnt = [0] * k

while tmp > 0:
    num = int(input())
    ans += num
    cnt[ans % k] += 1
    tmp -= 1

ans = cnt[0]
for i in range(k):
    ans += cnt[i] * (cnt[i] - 1) // 2

print(ans)
