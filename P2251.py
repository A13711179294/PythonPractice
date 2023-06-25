def monotone_min():
    head = 1
    tail = 0
    for i in range(1, n + 1):

        while head <= tail and q[tail] >= a[i]:
            tail -= 1
        tail += 1
        q[tail] = a[i]
        p[tail] = i
        while p[head] <= i - m:
            head += 1
        if m <= i:
            print(q[head])


n, m = map(int, input().split())
a = [0]
a.extend(list(map(int, input().split())))
q = [0] * (n + 1)
p = [0] * (n + 1)
monotone_min()

