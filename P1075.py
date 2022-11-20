n = int(input())

for x in range(2, n//2+1):
    p = n / x
    if p == int(p):
        print(int(p))
        break
