n, k = map(int, input().split())
A = []
B = []
for i in range(1, n + 1):
    if i % k == 0:
        A.append(i)
    else:
        B.append(i)

print('%.1f %.1f' % (sum(A) / len(A), sum(B) / len(B)))
