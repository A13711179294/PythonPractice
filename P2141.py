n = int(input())
ni = list(map(int, input().split()))
digit = []
for i in range(n):
    for j in range(i + 1, n):
        tmp = ni[i] + ni[j]
        if ni[i] + ni[j] in ni and ni[i] != tmp and ni[j] != tmp:
            digit.append(tmp)

print(len(set(digit)))
