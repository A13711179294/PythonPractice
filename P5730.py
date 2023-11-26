n = int(input().strip())
m = input().strip()
count = 0
num_a = ''
num_b = ''
num_c = ''
num_d = ''
num_e = ''
str = []
for i in m:
    count = count + 1
    if int(i) == 0:
        a = 'XXX'
        b = 'X.X'
        c = 'X.X'
        d = 'X.X'
        e = 'XXX'
    elif int(i) == 1:
        a = '..X'
        b = '..X'
        c = '..X'
        d = '..X'
        e = '..X'
    elif int(i) == 2:
        a = 'XXX'
        b = '..X'
        c = 'XXX'
        d = 'X..'
        e = 'XXX'
    elif int(i) == 3:
        a = 'XXX'
        b = '..X'
        c = 'XXX'
        d = '..X'
        e = 'XXX'
    elif int(i) == 4:
        a = 'X.X'
        b = 'X.X'
        c = 'XXX'
        d = '..X'
        e = '..X'
    elif int(i) == 5:
        a = 'XXX'
        b = 'X..'
        c = 'XXX'
        d = '..X'
        e = 'XXX'
    elif int(i) == 6:
        a = 'XXX'
        b = 'X..'
        c = 'XXX'
        d = 'X.X'
        e = 'XXX'
    elif int(i) == 7:
        a = 'XXX'
        b = '..X'
        c = '..X'
        d = '..X'
        e = '..X'
    elif int(i) == 8:
        a = 'XXX'
        b = 'X.X'
        c = 'XXX'
        d = 'X.X'
        e = 'XXX'
    elif int(i) == 9:
        a = 'XXX'
        b = 'X.X'
        c = 'XXX'
        d = '..X'
        e = 'XXX'
    if count == n:
        num_a = num_a + a
        num_b = num_b + b
        num_c = num_c + c
        num_d = num_d + d
        num_e = num_e + e
    else:
        num_a = num_a + a + '.'
        num_b = num_b + b + '.'
        num_c = num_c + c + '.'
        num_d = num_d + d + '.'
        num_e = num_e + e + '.'
str.append(num_a)
str.append(num_b)
str.append(num_c)
str.append(num_d)
str.append(num_e)
for i in str:
    print(i)