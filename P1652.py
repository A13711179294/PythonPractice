from math import sqrt

N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
r = list(map(int, input().split()))
x1, y1, x2, y2 = map(int, input().split())
count1 = 0
for i in range(N):
    if sqrt((x[i] - x1) ** 2 + (y[i] - y1) ** 2) < r[i] < sqrt((x[i] - x2) ** 2 + (y[i] - y2) ** 2):
        count1 += 1
    elif sqrt((x[i] - x2) ** 2 + (y[i] - y2) ** 2) < r[i] < sqrt((x[i] - x1) ** 2 + (y[i] - y1) ** 2):
        count1 += 1
print(count1)