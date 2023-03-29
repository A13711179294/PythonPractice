def main():
    class People:
        def __init__(self, cur, pre, next):
            self.cur = cur
            self.pre = pre
            self.next = next
            self.status = True

    def printf():
        start = li[0]
        while start.next != li[0]:
            start = start.next
            if start.status:
                print(start.cur, end=' ')

    n = int(input())
    li = [None] * (n + 1)
    li[0] = People(0, li[0], li[0])
    li[1] = People(1, li[0], li[0])
    li[0].next = li[1]
    li[0].pre = li[1]

    for i in range(2, n + 1):
        k, p = map(int, input().split())
        if p == 0:
            li[i] = People(i, li[k].pre, li[k])
            li[k].pre.next = li[i]
            li[k].pre = li[i]
        else:
            li[i] = People(i, li[k], li[k].next)
            li[k].next.pre = li[i]
            li[k].next = li[i]

    for _ in range(int(input())):
        x = int(input())
        li[x].status = False

    printf()


main()
