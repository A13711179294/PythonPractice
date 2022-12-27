M, N = map(int, input().strip().split())
temp = ''
for i in range(M, N + 1):
    temp += str(i)
print(temp.count('0'), temp.count('1'), temp.count('2'), temp.count('3'), temp.count('4'), temp.count('5'),
      temp.count('6'), temp.count('7'), temp.count('8'), temp.count('9'))
