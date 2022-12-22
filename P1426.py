s, x = map(int, input().strip().split())

speed = 7
distance = 0
begin = s - x
end = s + x

while True:
    if end > distance >= begin:
        distance += speed
        speed *= 0.98
        if distance > end:
            print('n')
            break
        else:
            print('y')
            break
    if distance > end:
        print('n')
        break
    distance += speed
    speed *= 0.98
