N = int(input())
tmp = N
score = []
student = []
while tmp > 0:
    tmp_std = tuple(input().split())
    student.append(tmp_std)
    sum1 = 0
    for i in tmp_std[1:4]:
        sum1 += int(i)
    score.append(sum1)
    tmp -= 1
for i in student[score.index(max(score))]:
    print(i, end=' ')
