n = int(input())
n //= 1000
hour = n % (24 * 60 * 60) // (60 * 60)
minutes = n % (60 * 60) // 60
second = n % 60
print('{:0>2d}:{:0>2d}:{:0>2d}'.format(hour, minutes, second))
