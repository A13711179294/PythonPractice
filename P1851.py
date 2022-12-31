a = [284, 1210, 2924, 5564, 6386, 10856, 14595, 18416, 66992, 71145, 76084, 87633, 88730]
b = [220, 1184, 2620, 5020, 6232, 10744, 12285, 17296, 66928, 67095, 63020, 69615, 79750]

s = int(input().strip())

# for i in range(s, 19000):
#     if i in a:
#         temp = a.index(i)
#         print(i, b[temp])
#         break
#     if i in b:
#         temp = b.index(i)
#         print(i, a[temp])
#         break

for i in range(0, 13):
    if s <= b[i]:
        print(b[i], a[i])
        break
    if s <= a[i]:
        print(a[i], b[i])
        break
