n = int(input().strip())
a = [0] + list(map(int, input().strip().split()))
b = [0] + list(map(int, input().strip().split()))
from1 = [i for i in range(n + 1)]
step = [1 for _ in range(n + 1)]
heap = [a[i] + b[1] for i in range(n + 1)]
sum1 = 1

while sum1 <= n:
    print(heap[1], end=' ')
    t = from1[1]
    step[t] += 1
    heap[1] = a[t] + b[step[t]]
    x = 1
    while x << 1 <= n:
        s = x << 1
        if s + 1 <= n and heap[s] > heap[s + 1]:
            s += 1
        if heap[x] > heap[s]:
            heap[x], heap[s] = heap[s], heap[x]
            from1[x], from1[s] = from1[s], from1[x]
            x = s
        else:
            break
    sum1 += 1