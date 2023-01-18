Mid = list(input().strip())
Pos = list(input().strip())
Pre = []


def test(mid, pos):
    if mid and pos:
        tmp = 0
        Pre.append(pos[-1])
        for i in range(len(mid)):
            if mid[i] == pos[-1]:
                tmp = i
        test(mid[0:tmp], pos[0:mid.index(pos[-1])])
        test(mid[tmp + 1:], pos[mid.index(pos[-1]):-1])
    else:
        return


test(Mid, Pos)
for i in Pre:
    print(i, end='')
