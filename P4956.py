n = int(input())
# n = 52(7x+21k)
flag = 0
for i in range(100, 0, -1):  # x
    for j in range(1, n // 1092 + 1):  # k
        if i * 7 * 52 + 52 * 21 * j == n:
            print(i)
            print(j)
            flag = 1
            break
    if flag == 1:
        break
