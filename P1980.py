n, x = map(int, input().split())
count1 = 0
for i in range(1, n + 1):
    count1 += str(i).count(str(x))
print(count1)
