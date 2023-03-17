import heapq

n = int(input())
a = list(map(int, input().split()))
li = []
for i in a:
    heapq.heappush(li, i)

ans = 0
for _ in range(n - 1):
    t1 = heapq.heappop(li)
    t2 = heapq.heappop(li)
    ans += t1 + t2
    heapq.heappush(li, t1 + t2)
print(ans)
