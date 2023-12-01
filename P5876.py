n = int(input())
li = [0]
min_length = 100

for _ in range(n):
    tmp = input()
    if len(tmp) < min_length:
        min_length = len(tmp)
    li.append(tmp)

for i in range(1, n + 1):
    for j in range(1, min_length + 1):
        flag = True
        t = li[i][:j]
        for k in range(1, n + 1):
            if i == k:
                continue
            if t == li[k][:j]:
                flag = False
                break
        if flag:
            print(t)
            break

