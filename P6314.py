a = []
sum1 = 0
for _ in range(9):
    tmp = int(input())
    a.append(tmp)
    sum1 += tmp

for i in range(9):
    for j in range(i + 1, 9):
        if sum1 - a[i] - a[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(a[k])
            break
