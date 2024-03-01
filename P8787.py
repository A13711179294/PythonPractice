from math import sqrt, floor


def main():
    n = int(input())
    h = [0] + list(map(int, input().split())) + [0]
    p = [0] * (n + 1)

    for i in range(1, n + 1):
        tmp = h[i]
        while tmp - 1:
            p[i] += 1
            tmp = floor(sqrt(tmp // 2 + 1))

    cnt = 0
    for i in range(max(p), 0, -1):
        for j in range(1, n + 1):
            if p[j] == i:
                if h[j] != h[j + 1]:
                    cnt += 1
                p[j] -= 1
                h[j] = floor(sqrt(h[j] // 2 + 1))

    print(cnt)


main()
