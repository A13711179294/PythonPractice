from math import sqrt


def is_square(n):
    for i in range(1, int(sqrt(n) + 1)):
        if i * i == n:
            return True
    else:
        return False


a, b = map(int, input().split())
# for i in range(a, b + 1):
#     if is_square(i):
#         for j in range(1, len(str(i))):
#             if is_square(int(str(i)[:j])) and is_square(int(str(i)[j:])):
#                 print(i)
#                 break
li = [49, 169, 361, 1225, 1444, 1681, 3249, 4225, 4900, 9025,
      15625, 16900, 36100, 42025, 49729, 64009, 81225, 93025,
      105625, 122500, 144400, 168100, 225625, 237169, 256036,
      324900, 422500, 490000, 519841, 576081, 819025, 902500,
      950625, 970225]

for i in range(a, b + 1):
    if i in li:
        print(i)
