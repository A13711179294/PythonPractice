n, m = map(int, input().split())

dirs = []
pro = []

for _ in range(n):
    b, c = input().split()
    dirs.append(int(b))
    pro.append(c)

cur = 0
for _ in range(m):
    a, s = map(int, input().split())
    if dirs[cur] == a:
        s *= -1
    cur = (cur + n + s) % n

print(pro[cur])
