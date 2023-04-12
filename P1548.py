N, M = map(int, input().split())
matrix = [[0] for i in range(M) for j in range(N)]
square_count = 0
rectangle_count = 0
for i in range(N):
    for j in range(M):
        for x in range(i, N):
            for y in range(j, M):
                if x - i == y - j:
                    square_count += 1
                else:
                    rectangle_count += 1

print(square_count, rectangle_count)