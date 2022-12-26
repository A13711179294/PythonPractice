n = int(input().strip())

count = 0
unhappy = 0
sum1 = 0

while count < n:
    a, b = map(int, input().strip().split())
    unhappy += a + b - 8
    sum1 += unhappy
    count += 1

print(sum1)
