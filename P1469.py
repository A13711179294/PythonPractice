n = int(input())
m = list(map(int, input().split()))
tmp = set(m)
for i in tmp:
    if m.count(i) % 2 != 0:
        print(i)