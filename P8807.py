for _ in range(int(input())):
    n, m = map(int, input().split())
    if m > n + 1:
        print('Yes')
    else:
        for i in range(1, m + 1):
            if n % i != i - 1:
                print('Yes')
                break
        else:
            print('No')