n = int(input())
w = list(map(int, input().split()))
w.sort()
ans = 0
while len(w) > 1:
    tmp = w[0] + w[-1]
    ans += w[0] * w[-1]
    w.pop(0)
    w.pop(-1)
    w.append(tmp)

print(ans)
