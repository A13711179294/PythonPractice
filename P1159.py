class song:
    def __init__(self, name, status):
        self.name = name
        self.status = status


N = int(input().strip())
tmp = 0
song_list = []
flag = [0] * N
res = [0] * N
while tmp < N:
    name = input().strip()
    status = input().strip()
    song_list.append(song(name, status))
    if status == 'SAME':
        res[tmp] = name
        flag[tmp] = 1
    tmp += 1

tmp = 0
for i in song_list:
    if i.status == 'DOWN':
        for j in range(N):
            if res[j] == 0:
                res[j] = i.name
                tmp = j
                break

for i in song_list:
    if i.status == 'UP':
        for j in range(N):
            if res[j] == 0:
                res[j] = i.name
                break

for i in res:
    print(i)
