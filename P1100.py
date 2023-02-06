n = bin(int(input())).lstrip('0b')
tmp = '{:0>32s}'.format(n)
new = tmp[16:33] + tmp[0:16]
print(int(new, 2))
