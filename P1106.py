n = list(input().strip())
n.append('0')
k = int(input().strip())
count = 0
i = 0
while count != k:
    if int(n[i]) > int(n[i + 1]):
        n.remove(n[i])
        count += 1
        i = 0
    else:
        i += 1

print(int(''.join(n[:-1])))
