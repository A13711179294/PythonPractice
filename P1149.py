n = int(input())
if n - 4 <= 0:
    print(0)
else:
    f = [0] * 2224
    f[0] = 6
    f[1] = 2
    f[2] = 5
    f[3] = 5
    f[4] = 4
    f[5] = 5
    f[6] = 6
    f[7] = 3
    f[8] = 7
    f[9] = 6

    for i in range(10, 100):
        f[i] = f[int(i // 10)] + f[i % 10]
    for i in range(100, 1000):
        f[i] = f[int(i // 100)] + f[(i - int(i // 100) * 100) // 10] + f[i % 10]
    for i in range(1000, 1113):
        f[i] = f[int(i // 1000)] + f[(i - int(i // 1000) * 1000) // 100] + f[(i - int(i // 100) * 100) // 10] + f[
            i % 10]
    total = 0
    for a in range(0, 1112):
        for b in range(0, 1112):
            if a + b > 1112:
                break
            if f[a] + f[b] + f[a + b] == n - 4:
                total += 1

    print(total)
