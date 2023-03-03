N = int(input())
graph1 = [[0 for j in range(N + 1)] for i in range(N + 1)]
tmp = 1
while tmp <= N:
    digit = list(map(int, input().split()))
    count1 = 1
    for i in digit:
        graph1[tmp][count1] = i
        count1 += 1
    tmp += 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        graph1[i][j] = max(graph1[i - 1][j], graph1[i - 1][j - 1]) + graph1[i][j]

tmp = 0
for i in graph1[-1]:
    if i > tmp:
        tmp = i
print(tmp)
