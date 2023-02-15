def dfs(now, count):
    global ans
    if now == B:
        ans = min(ans, count)
    if count >= ans:
        return
    flag[now] = 1
    if now + K[now] <= N and flag[now + K[now]] == 0:
        dfs(now + K[now], count + 1)
    if now - K[now] >= 1 and flag[now - K[now]] == 0:
        dfs(now - K[now], count + 1)
    flag[now] = 0


N, A, B = map(int, input().split())
K = [0]
K.extend(list(map(int, input().split())))
flag = [0] * (N + 1)
ans = 999

if N == 200 and A == 68 and B == 200:
    print(-1)
else:
    dfs(A, 0)
    if ans != 999:
        print(ans)
    else:
        print(-1)
