a, b, c, d = map(float, input().split())

x = -100
x_list = []
while x <= 100:
    temp = round(x, 2)
    if abs(a * pow(temp, 3) + b * pow(temp, 2) + c * temp + d) < 1e-7:
        x_list.append(temp)
    x += 0.01

for i in x_list:
    print('%.2f' % i, end=' ')
