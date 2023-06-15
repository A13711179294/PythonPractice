from sys import setrecursionlimit, stdin, stdout

setrecursionlimit(1000000)


def main():
    global ans

    def dfs(last):
        global ans, x, y
        for i in range(last, n + 1):
            if not vis[i]:
                x *= S[i]
                y += B[i]
                ans = min(ans, abs(x - y))
                vis[i] = True
                dfs(i)
                x //= S[i]
                y -= B[i]
                vis[i] = False

    n = int(stdin.readline())

    vis = [False] * (n + 1)
    S = [0]
    B = [0]
    for _ in range(n):
        s, b = map(int, stdin.readline().split())
        S.append(s)
        B.append(b)

    dfs(1)
    stdout.write(str(ans))


ans = 0xfffffff
x = 1
y = 0
main()
