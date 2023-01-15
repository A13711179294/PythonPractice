dict1 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
N = int(input().strip())
M = list(input().strip())

for i in range(len(M) - 1):
    if M[i] in dict1:
        M[i] = dict1[M[i]]

count1 = 0

def test(m1):
    flag = 0
    global count1
    m2 = list(reversed(m1))
    m3 = []
    add = 0

    for i in range(len(m1) - 1, -1, -1):
        tmp = ((int(m1[i]) + int(m2[i])) + add) % N
        add = ((int(m1[i]) + int(m2[i])) + add - tmp) // N
        m3.append(tmp)
    if add != 0:
        m3.append(add)
    left = 0
    right = len(m3) - 1
    while left < right:
        if m3[left] != m3[right]:
            flag = 1
            break
        left += 1
        right -= 1
    count1 += 1
    if flag == 1 and count1 <= 30:
        test(m3)


if M != 0:
    test(M)
if count1 <= 30:
    print('STEP=%d' % count1)
else:
    print('Impossible!')
