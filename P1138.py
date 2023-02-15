n, k = map(int, input().split())
digit = set(map(int, input().split()))
if len(digit) < k:
    print('NO RESULT')
else:
    tmp = k
    count1 = 0
    while tmp > 1:
        digit.remove(min(digit))
        tmp -= 1
        count1 += 1
    print(min(digit))
