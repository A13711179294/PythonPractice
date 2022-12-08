# 请统计某个给定范围[L, R][L,R]的所有整数中，数字 22 出现的次数。
# 比如给定范围[2, 22][2,22]，数字22 在数 22中出现了 11 次，在数1212 中出现 11 次，在数 2020 中出现 11次，
# 在数 21 中出现 11 次，在数 2222 中出现 22次，所以数字22 在该范围内一共出现了 66次。

L, R = map(int, input().split())
sum = 0
for item in range(L, R + 1):
    StrItem = str(item)
    ItemSum = StrItem.count('2')
    sum += ItemSum
print(sum)