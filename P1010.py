str1 = ''
def test(num):
    global str1
    tmp1 = str(bin(num)).lstrip('0b')
    flag = 1
    for i in range(len(tmp1)):

        if int(tmp1[i]) != 0:
            tmp2 = len(tmp1) - i - 1
            if tmp2 == 0:
                if flag == 0:
                    str1 += '+'
                str1 += '2(0)'
            elif tmp2 == 1:
                if flag == 0:
                    str1 += '+'
                str1 += '2'
            elif tmp2 == 2:
                if flag == 0:
                    str1 += '+'
                str1 += '2(2)'
            else:
                if flag == 0:
                    str1 += '+'
                str1 += '2('
                test(len(tmp1) - i - 1)
                str1 += ')'
            flag = 0


n = int(input())
test(n)

print(str1)
