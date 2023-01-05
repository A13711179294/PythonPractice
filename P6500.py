a, b = input().split()
a_min = ''
b_min = ''
a_max = ''
b_max = ''

for i in range(len(a)):
    if a[i] == '5':
        a_max += '6'
    else:
        a_max += a[i]

for i in range(len(b)):
    if b[i] == '5':
        b_max += '6'
    else:
        b_max += b[i]

for i in range(len(a)):
    if a[i] == '6':
        a_min += '5'
    else:
        a_min += a[i]

for i in range(len(b)):
    if b[i] == '6':
        b_min += '5'
    else:
        b_min += b[i]

print(int(a_min) + int(b_min), int(a_max) + int(b_max))
