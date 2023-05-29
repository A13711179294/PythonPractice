n, m, k, r = map(int, input().strip().split())
dp = [0 for _ in range(r + 1)]
title_time = [0]
homework_time = [0]
value = [0]

title_time.extend(list(map(int, input().strip().split())))
homework_time.extend(list(map(int, input().strip().split())))
value.extend(list(map(int, input().strip().split())))

title_time.sort()

for i in range(1, m + 1):
    for j in range(r, homework_time[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - homework_time[i]] + value[i])

cnt = 0

for i in range(1, r + 1):
    if dp[i] >= k:
        cnt = r - i
        break

ans = 0
for i in title_time[1:]:
    if cnt >= i:
        cnt -= i
        ans += 1
    else:
        break
print(ans)

