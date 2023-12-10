N = int(input())
b = list(map(int, input().split()))

max_number = max(b)
ans = 0

for i in range(0, N):
    a = b.copy()
    cnt = 0
    count = 1
    while True:
        if a[i] == count:
            cnt += a[i]
            a.pop(i)
            count = 1
        else:
            i += 1
            count += 1

        if i == len(a):
            i = 0
        if count > max_number or len(a) <= 0:
            if cnt > ans:
                ans = cnt
            break

print(ans)
