from math import gcd

a = list(map(int, input().split()))
gcd1 = gcd(min(a), max(a))

print(str(int(min(a)//gcd1)) + '/' + str(int(max(a)//gcd1)))
