from queue import PriorityQueue


n, m = map(int, input().split())
q = PriorityQueue(m)
for _ in range(n):
    a, b, c = map(int, input().split())
    for x in range(1, m + 1):
        sum1 = a * (x ** 2) + b * x + c
        if q.qsize() < m:
            q.put(-sum1)
        else:
            tmp = q.get()
            if tmp < -sum1:
                q.put(-sum1)
            else:
                q.put(tmp)
                break

ans = []
for _ in range(m):
    ans.append(-q.get())

print(*ans[::-1])