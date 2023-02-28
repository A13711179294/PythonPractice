def find(x):
    if pre[x] == x:
        return x
    pre[x] = find(pre[x])
    return pre[x]


def join(x, y):
    t1 = find(pre[x])
    t2 = find(pre[y])
    if t1 != t2:
        pre[t1] = t2
        return True


N, M, K = map(int, input().split())
pre = [0]
for i in range(1, N + 1):
    pre.append(i)

cloud = []
tmp = M
while tmp > 0:
    cloud.append(tuple(map(int, input().split())))
    tmp -= 1
cloud.sort(key=lambda x: x[2])

count = N
ans = 0
for i in range(len(cloud)):
    ret = join(cloud[i][0], cloud[i][1])
    if ret:
        ans += cloud[i][2]
        count -= 1
        if count == K:
            break
print(ans)
