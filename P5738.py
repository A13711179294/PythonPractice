n, m = map(int, input().split())
tmp1 = n
score = []
while tmp1 > 0:
    tmp2 = list(map(int, input().split()))
    tmp2.remove(max(tmp2))
    tmp2.remove(min(tmp2))
    score.append(sum(tmp2) / (m - 2))
    tmp1 -= 1

print('%.2f' % max(score))
