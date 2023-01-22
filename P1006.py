m, n = map(int, input().strip().split())
graph1 = [[[0 for _ in range(60)] for _ in range(60)] for _ in range(120)]
graph2 = [[0 for _ in range(120)] for _ in range(120)]

for i in range(1, m + 1):
    tmp = map(int, input().strip().split())
    j = 1
    for value in tmp:
        graph2[i][j] = value
        j += 1

for k in range(3, m + n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i < k and j < k:
                graph1[k][i][j] = max(graph1[k - 1][i][j], graph1[k - 1][i - 1][j], graph1[k - 1][i][j - 1],
                                      graph1[k - 1][i - 1][j - 1]) + graph2[k - i][i] + graph2[k - j][j]
                if i == j:
                    graph1[k][i][j] -= graph2[k - j][j]

print(graph1[m + n][n][n])
