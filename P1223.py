n = int(input())
T = list(map(int, input().split()))
for i in range(n):
    T[i] = T[i] * 1001 + i
T.sort()
sum1 = 0
pre = 0
for i in range(n):
    print(T[i] % 1001 + 1, end=' ')
    sum1 += pre
    pre += T[i] // 1001
print()
print('%.2f' % (sum1 / n))
