class student:
    def __init__(self, no, score1, score2):
        self.no = no
        self.score1 = score1
        self.score2 = score2
        self.score3 = score1 * 0.7 + score2 * 0.3
        self.score4 = score1 + score2

    def status(self):
        if self.score1 * 7 + self.score2 * 3 >= 800 and self.score4 > 140:
            print('Excellent')
        else:
            print('Not excellent')

    def __str__(self):
        return self.score4


N = int(input())
tmp = N
stu = []
while tmp > 0:
    no, s1, s2 = map(int, input().split())
    tmp_stu = student(no, s1, s2)
    stu.append(tmp_stu)
    tmp -= 1

for i in stu:
    i.status()
