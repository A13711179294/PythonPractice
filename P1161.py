# n = int(input())
# lamp = {}
#
# for _ in range(n):
#     begin, count = map(float, input().split())
#     for j in range(1, int(count) + 1):
#         lamp[int(begin * j)] = lamp.get(int(begin * j), False)
#         if not lamp[int(begin * j)]:
#             lamp[int(begin * j)] = True
#         else:
#             lamp[int(begin * j)] = False
#
# print(max(lamp, key=lamp.get))

n = int(input())
lamp = [0] * 2000001

for _ in range(n):
    begin, count = map(float, input().split())
    for j in range(1, int(count) + 1):
        if not lamp[int(begin * j)]:
            lamp[int(begin * j)] = 1
        else:
            lamp[int(begin * j)] = 0

print(lamp.index(1))
