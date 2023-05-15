d = [[0, 0, 0, 0, 0, 0],
     [0, 5, -1, -2, -1, -3],
     [0, -1, 5, -3, -2, -4],
     [0, -2, -3, 5, -2, -2],
     [0, -1, -2, -2, 5, -1],
     [0, -3, -4, -2, -1, 0]]

n1, s1 = input().split()
n2, s2 = input().split()
n1 = int(n1)
n2 = int(n2)
dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
s1 = [0] + list(s1)
s2 = [0] + list(s2)

for i in range(1, n1 + 1):
    if s1[i] == 'A':
        s1[i] = 1
    elif s1[i] == 'C':
        s1[i] = 2
    elif s1[i] == 'G':
        s1[i] = 3
    else:
        s1[i] = 4

for i in range(1, n2 + 1):
    if s2[i] == 'A':
        s2[i] = 1
    elif s2[i] == 'C':
        s2[i] = 2
    elif s2[i] == 'G':
        s2[i] = 3
    else:
        s2[i] = 4

for i in range(1, n1 + 1):
    dp[i][0] = dp[i - 1][0] + d[s1[i]][5]

for i in range(1, n2 + 1):
    dp[0][i] = dp[0][i - 1] + d[5][s2[i]]

for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        dp[i][j] = max(dp[i - 1][j - 1] + d[s1[i]][s2[j]], dp[i - 1][j] + d[s1[i]][5], dp[i][j - 1] + d[5][s2[j]])

# for i in dp:
#     print(i)

print(dp[n1][n2])
