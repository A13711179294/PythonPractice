n = list(map(int, input().split()))
str1 = input()
n.sort()
for i in str1:
    if i == 'A':
        print(n[0], end=' ')
    if i == 'B':
        print(n[1], end=' ')
    if i == 'C':
        print(n[2], end=' ')