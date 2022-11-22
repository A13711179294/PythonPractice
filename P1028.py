n = int(input().strip())
n_list = [0, 1, 2, 2]
for i in range(4, n + 1):
    n_list.append(1)
    for x in range(0, i//2 + 1):
        n_list[i] += n_list[x]

print(n_list[n])
