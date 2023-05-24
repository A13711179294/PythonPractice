n = int(input())
a = [0] + list(map(int, input().strip().split()))
a += [0] * 1000

dic = {}
for i in range(1, n + 1):
    dic[a[i]] = i

for _ in range(int(input().strip())):
    print(dic.get(int(input()), 0))
