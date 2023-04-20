n = int(input().strip())
sum1 = 0
f = [0] * 21
f[1] = 0
f[2] = 1
f[3] = 2
for i in range(4, n + 1):
    f[i] = ((i - 1) * (f[i - 1] + f[i - 2]))
#print(f)
print(f[n])
