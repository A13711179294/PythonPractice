from sys import stdin, stdout


def main():
    def check(l):
        sum1 = 0
        for i in a:
            if i > l:
                sum1 += i - l
        if sum1 >= m:
            return True
        return False

    n, m = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))

    left = 1
    right = max(a)
    while left < right:
        mid = left + right + 1 >> 1
        if check(mid):
            left = mid
        else:
            right = mid - 1
    stdout.write(str(left))


main()