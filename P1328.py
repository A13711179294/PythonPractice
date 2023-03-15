N, NA, NB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
score = [[0, 0, 1, 1, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [1, 1, 0, 0, 0]]

chooseA = 0
chooseB = 0
countA = 0
countB = 0
for i in range(N):
    tmp1 = A[chooseA]
    tmp2 = B[chooseB]
    countA += score[tmp1][tmp2]
    countB += score[tmp2][tmp1]
    chooseA += 1
    chooseB += 1
    if chooseA == NA:
        chooseA = 0
    if chooseB == NB:
        chooseB = 0

print(countA, countB, sep=' ')
