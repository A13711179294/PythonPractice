N, S = map(int, input().split())
last, C = map(int, input().split())
ans = last * C
tmp = N - 1
while tmp > 0:
    C, Y = map(int, input().split())
    last = min(last + S, C)
    ans += last * Y
    tmp -= 1
print(ans)