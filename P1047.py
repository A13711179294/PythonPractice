l, m = map(int, input().split())
TreeList = list('1' * (l + 1))

for i in range(m):
    u, v = map(int, input().split())
    TreeList[u:v+1] = '0'*(v-u+1)

print(TreeList.count('1'))