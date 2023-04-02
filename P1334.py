import heapq

n = int(input())
li = []
for _ in range(n):
    heapq.heappush(li, int(input()))

sum1 = 0
for _ in range(n - 1):
    t1 = heapq.heappop(li)
    t2 = heapq.heappop(li)
    sum1 += t1 + t2
    heapq.heappush(li, t1 + t2)

print(sum1)