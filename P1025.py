n, k = map(int, input().split())

n_list = []
count = 0
for x in range(1, n):
    for y in range(1, x + 1):
        for z in range(1, y + 1):
            if x + y + z == n:
                print(x, y, z)
                count += 1
print(count)
