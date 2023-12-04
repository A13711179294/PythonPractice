t = int(input())
tmp = t
while tmp > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    tmp_a = a.copy()
    tmp_b = b.copy()
    tmp_a.sort()
    tmp_b.sort()
    if tmp_a != tmp_b:
        print('NO')
    else:
        print('YES')
        for i in range(0, n):
            if a[i] != b[i]:
                for j in range(i, n):
                    if a[j] == b[i]:
                        k = j
                        while k != i:
                            print(k, k + 1)
                            a[k], a[k - 1] = a[k - 1], a[k]
                            k -= 1
                        break
        print(0, 0)
    tmp -= 1
