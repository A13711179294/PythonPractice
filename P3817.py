n, x = map(int, input().split())
ai = list(map(int, input().split()))
count1 = 0
for i in range(1, n):
    if ai[i] + ai[i-1] > x:
        count1 += ai[i] + ai[i - 1] - x
        if ai[i] > (ai[i] + ai[i - 1] - x):
            ai[i] -= (ai[i-1] + ai[i] - x)
        else:
            ai[i] = 0

print(count1)