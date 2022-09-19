# 问题：编写一个程序，接受一系列逗号分隔的4位二进制数作为输入，然后检查它们是否可被5整除。 可被5整除的数字将以逗号分隔的顺序打印。
# 例：
# 0100,0011,1010,1001
# 那么输出应该是：
# 1010
# 注意：假设数据由控制台输入。
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。
value = []
print('请输入逗号分隔的4位二进制数：')
items = [x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    # print(intp)
    if not intp % 5:
        value.append(p)

print(','.join(value))