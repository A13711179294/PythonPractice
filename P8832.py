def main():
    n = int(input().strip())
    people = []
    for i in range(1, n + 1):
        t, k = map(int, input().strip().split())
        people.append((i, t, k))

    people.sort(key=lambda x: (x[1] * x[2], x[1], -x[0]), reverse=True)
    for i in people:
        print(i[0], end=' ')


if __name__ == '__main__':
    main()