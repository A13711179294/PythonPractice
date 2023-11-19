from math import ceil

s, v = map(int, input().split())
t = ceil(s / v) + 10
tmp1 = t % 60
tmp2 = t // 60
M = 60 - tmp1
H = 7 - tmp2
if M == 60:
    M = 0
    H += 1
if H < 0:
    H = 24 + H
print('{:0>2d}:{:0>2d}'.format(H, M))
