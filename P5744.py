class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


n = int(input())
li = []
for _ in range(n):
    tmp = list(input().split())
    li.append(Student(tmp[0], int(tmp[1]), int(tmp[2])))

for i in range(n):
    t1 = li[i].age + 1
    t2 = li[i].score * 1.2

    print(li[i].name, end=' ')
    if t1 == int(t1):
        print(int(t1), end=' ')
    else:
        print(t1, end=' ')
    if t2 == int(t2):
        t2 = int(t2)
    if t2 > 600:
        t2 = 600
    print(t2)
