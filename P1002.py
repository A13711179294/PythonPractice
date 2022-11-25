Bx, By, Cx, Cy = map(int, input().strip().split())
Bx += 2
By += 2
Cx += 2
Cy += 2
M_X = [Cx, Cx - 2, Cx - 1, Cx - 2, Cx - 1, Cx + 1, Cx + 2, Cx + 1, Cx + 2]
M_Y = [Cy, Cy - 1, Cy - 2, Cy + 1, Cy + 2, Cy + 2, Cy + 1, Cy - 2, Cy - 1]
M_dict = zip(M_X, M_Y)

chessboard = [[] for _ in range(25)]
M_chessboard = [[] for _ in range(25)]

for x in range(25):
    for y in range(25):
        M_chessboard[x].append(0)
        chessboard[x].append(0)

chessboard[2][1] = 1

for key, value in M_dict:
    M_chessboard[key][value] = 1

for i in range(2, Bx + 1):
    for j in range(2, By + 1):
        if M_chessboard[i][j] == 1:
            continue
        chessboard[i][j] = chessboard[i - 1][j] + chessboard[i][j - 1]

# for i in range(24):
#     print(chessboard[i])

print(chessboard[Bx][By])
