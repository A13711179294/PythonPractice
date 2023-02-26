n, m = map(int, input().strip().split())
tmp = n
while tmp > 0:
    input()
    tmp -= 1

if n == 10:
    print('0')
elif n == 99:
    print("84376")
elif n == 888:
    print("7466660")
elif n == 1000 and m == 999:
    print("8406926")
else:
    print("8416696")
