A, B, C = map(int, input().split())
tmp = A * 0.2 + B * 0.3 + C * 0.5
if tmp == int(tmp):
    print(int(tmp))
else:
    print(tmp)