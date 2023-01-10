a, b = input().split()
a1 = list(reversed(a))
b1 = list(reversed(b))
a1 = ''.join(a1)
b1 = ''.join(b1)
if a1 > b1:
    print(a1)
else:
    print(b1)
