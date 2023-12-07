def location(num):
    y = num // w + 1
    x = num % w
    if x == 0:
        x = w
    if y % 2 == 0:
        x = w - x + 1
    return x, y


w, m, n = map(int, input().split())
x1, y1 = location(n)
x2, y2 = location(m)
print(abs(y1-y2) + abs(x1-x2))
