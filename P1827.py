def find(mid):
    if mid:
        tmp = 0
        for i in range(len(mid)):
            if mid[i] == Pre[0]:
                tmp = i
                break
        Pre.pop(0)
        find(mid[0: tmp])
        find(mid[tmp + 1:])
        Pos.append(mid[tmp])
    else:
        return


Mid = list(input().strip())
Pre = list(input().strip())
Pos = []
find(Mid)
for i in Pos:
    print(i, end='')
