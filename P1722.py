n = int(input())
f = [0] * 101
f[0] = f[1] = 1
for i in range(2, n + 1):
    for j in range(1, i + 1):
        f[i] += f[j - 1] * f[i - j]
        f[i] %= 100

print(f[n])