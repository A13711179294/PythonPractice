from queue import PriorityQueue

n = int(input())
a = [0] + list(map(int, input().split()))
q1 = PriorityQueue()  # 大根堆
q2 = PriorityQueue()  # 小根堆
mid = a[1]
print(a[1])
for i in range(2, n + 1):
    if a[i] > mid:
        q2.put(a[i])
    else:
        q1.put(-a[i])
    if i % 2 == 1:
        while q1.qsize() != q2.qsize():
            if q1.qsize() > q2.qsize():
                q2.put(mid)
                mid = -q1.get()
            else:
                q1.put(-mid)
                mid = q2.get()
        print(mid)