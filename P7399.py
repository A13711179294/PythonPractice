n = int(input())
a = list(map(int, input().split()))
stack = []
ans = 0
for i in range(n):
    while stack and a[i] < stack[-1]:
        stack.pop()
    if stack and stack[-1] == a[i]:
        continue
    if a[i]:
        ans += 1
        stack.append(a[i])

print(ans)
