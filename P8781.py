N = int(input())
for i in range(1, N + 1):
    print(max((N - i), i - 1) * 2)
