def isprime(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


dict1 = {}

str1 = input()
for i in str1:
    dict1[i] = dict1.get(i, 0) + 1

maxn = dict1[max(dict1, key=dict1.get)]
minn = dict1[min(dict1, key=dict1.get)]
tmp = maxn - minn

if tmp <= 1:
    print('No Answer')
    print(0)
elif isprime(tmp) or tmp == 2:
    print('Lucky Word')
    print(tmp)
else:
    print('No Answer')
    print(0)
