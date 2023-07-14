n = int(input().strip())
c = str(n).count('9')
if c == len(str(n)):
    s = ''
    for i in range(c * 9):
        s += '1'
    print(int(s) // n, s)
else:
    i = 2
    flag = 0
    if n % 2 == 0:
        flag = 1
    while True:
        if int(bin(i).lstrip('0b')) % n == 0:
            tmp1 = int(bin(i).lstrip('0b'))
            tmp2 = int(bin(i).lstrip('0b')) // n
            break
        else:
            if flag == 0:
                i += 1
            else:
                i += 2

    print(tmp2, tmp1)
