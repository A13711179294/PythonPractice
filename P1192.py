N, K = map(int, input().split())
step = [1, 1]
flag = 0
tmp = 1
for i in range(1, N):
    if flag == 1:
        tmp = (tmp - step[i - K] + step[i]) % 100003
        step.append(tmp)
    else:
        sum1 = 0
        for j in range(0, K):
            if i >= j and flag == 0:
                sum1 = (step[i - j] + sum1) % 100003
                if j == K - 1:
                    flag = 1
                    tmp = sum1
        step.append(sum1)
print(step[N])
