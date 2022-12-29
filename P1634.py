x, n = map(int, input().split())
count = 1

for i in range(1, n + 1):
    count = count * x + count

print(count)