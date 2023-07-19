count1 = {}
s1, s2, s3 = map(int, input().split())
for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            count1[i + j + k] = count1.get(i + j + k, 0) + 1

print(max(count1, key=count1.get))
