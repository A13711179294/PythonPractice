n, s = map(int, input().split())

add = [0] * (n + 1)
count = 1
while True:
    add[0] = count
    for i in range(1, n + 1):
        add[i] = add[i - 1] * 2 - 1
    if sum(add) == s:
        break
    elif sum(add) < s:
        count += 1

print(count)
