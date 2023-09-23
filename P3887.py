from queue import PriorityQueue

k, d, m, f = map(int, input().split())
ki = list(map(int, input().split()))
di = list(map(int, input().split()))
mi = list(map(int, input().split()))
fi = list(map(int, input().split()))
k_queue = PriorityQueue(k)
d_queue = PriorityQueue(d)
m_queue = PriorityQueue(m)
f_queue = PriorityQueue(f)

for i in ki:
    k_queue.put(-i)
for i in di:
    d_queue.put(-i)
for i in mi:
    m_queue.put(-i)
for i in fi:
    f_queue.put(-i)

for _ in range(int(input())):
    sum1 = 0
    a, b, c = map(int, input().split())
    sum1 += -k_queue.get()
    for _ in range(a):

        sum1 += -d_queue.get()
    for _ in range(b):
        sum1 += -m_queue.get()
    for _ in range(c):
        sum1 += -f_queue.get()
    print('%.2f' % (sum1 / 11))


