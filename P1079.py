K = list(input().strip())
C = list(input().strip())
M = []

K = [i.lower() for i in K]
K_len = len(K)

K1 = 0
for i in C:
    if i.isupper():
        tmp = 65 + (ord(i) - ord(K[K1].upper())) % 26
    else:
        tmp = 97 + (ord(i) - ord(K[K1])) % 26
    M.append(chr(tmp))
    if K1 == (K_len - 1):
        K1 = 0
    else:
        K1 += 1

for i in M:
    print(i, end='')
