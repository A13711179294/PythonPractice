N = int(input())
tmp = N
Ki = []
while tmp > 0:
    Ki.extend(input())
    tmp -= 1
print(Ki.count('A')*4+Ki.count('K')*3+Ki.count('Q')*2+Ki.count('J')*1)
