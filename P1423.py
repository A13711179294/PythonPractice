s = float(input())
distance = 0
forward = 2
count = 1
while distance < s:
    distance += forward
    forward *= 0.98
    count += 1
print(count - 1)
