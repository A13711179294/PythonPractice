n, m = map(int, input().strip().split())
hole = list(map(int, input().strip().split()))
distance = []
for i in range(n - 1):
    distance.append(hole[i + 1] - hole[i])
# print(distance)
distance.sort()
ans = 0
for i in distance[:n - m]:
    ans += i
# print(hole)
# print(distance)
print(ans + m)