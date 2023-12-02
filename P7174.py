n = list(input())
sum1 = 0
for i in range(len(n)):
    n[i] = int(n[i])
    sum1 += n[i]
n.sort(reverse=True)

if n[-1] != 0 or sum1 % 3 != 0:
    print('-1')
else:
    for i in n:
        print(i, end='')