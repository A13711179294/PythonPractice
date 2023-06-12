from sys import setrecursionlimit

setrecursionlimit(1000000)
ans = str(eval(input()))
if len(ans) > 4:
    print(int(ans[-4:]))
else:
    print(ans)
