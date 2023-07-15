from collections import deque

n = int(input())
stack = deque()
ans = 0
for _ in range(n):
    x = int(input())
    while stack and stack[-1] <= x:
        stack.pop()
    ans += len(stack)
    stack.append(x)
print(ans)
