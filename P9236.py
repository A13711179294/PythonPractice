n = int(input())
a = [0] + list(map(int, input().split()))
q = [0] * (n + 1)
cnt = [0, 0]
sum1 = 0
for i in range(0, 21):
    for j in range(1, n + 1):
        if (a[j] >> i) & 1:
            q[j] = q[j - 1] ^ 1
        else:
            q[j] = q[j - 1]

    cnt[0] = cnt[1] = 0
    for j in range(0, n + 1):
        cnt[q[j]] += 1
    sum1 += (1 << i) * cnt[0] * cnt[1]

print(sum1)