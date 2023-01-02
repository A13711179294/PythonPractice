n = int(input())
wands = list(map(int, input().split()))
boxes = list(map(int, input().split()))
wands.sort()
boxes.sort()
for i in range(n):
    if wands[i] > boxes[i]:
        print('NE')
        break
else:
    print('DA')
