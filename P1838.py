cheer = input().strip()

win_cheer = ['123', '456', '789', '147', '258', '369', '159', '357']
cheer_length = len(cheer)
flag = 0

if cheer_length == 9:
    xiaoa = cheer[0] + cheer[2] + cheer[4] + cheer[6] + cheer[8]
    for x in range(0, 5):
        for y in range(x + 1, 5):
            for z in range(y + 1, 5):
                if xiaoa[x] + xiaoa[y] + xiaoa[z] in win_cheer:
                    print('xiaoa wins.')
                    flag = 1
                    break
    if flag == 0:
        print('drew.')
else:
    if cheer_length % 2 == 0:
        print('uim wins.')
    else:
        print('xiaoa wins.')
