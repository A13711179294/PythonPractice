n = int(input())
h = [0] + list(map(int, input().split()))
h.sort()

ans = 0
l = 0
r = n
while l < r:
    ans += (h[l] - h[r]) * (h[l] - h[r])
    l += 1
    ans += (h[l] - h[r]) * (h[l] - h[r])
    r -= 1

print(ans)
