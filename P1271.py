n, m = map(int, input().split())
ticket = list(map(int, input().split()))
ticket.sort()
for i in ticket:
    print(i, end=' ')
