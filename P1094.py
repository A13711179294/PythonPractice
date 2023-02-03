w = int(input())
n = int(input())
tmp = n
G = []

while tmp > 0:
    G.append(int(input()))
    tmp -= 1

G.sort()

count1 = 0
len1 = 0
len2 = len(G) - 1

while len1 <= len2:
    while G[len1] + G[len2] <= w:
        G[len1] = 0
        G[len2] = 0
        count1 += 1
        len1 += 1
        break
    len2 -= 1

print(count1 + len(G) - G.count(0))
