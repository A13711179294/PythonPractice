t = int(input().strip())
tmp = t
while tmp > 0:
    n, m = map(int, input().strip().split())
    a = input().strip().lower()
    b = input().strip().lower()
    la = len(a)
    lb = len(b)
    ans = 0
    for i in range(0, lb - la + 1):
        if b[i:i + la] == a:
            ans += 1
    print(ans)
    tmp -= 1
