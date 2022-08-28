# 问题:
# 编写一个程序，根据给定的公式计算并打印值:。以下是C和H的固定值:C是50。H是30。D是一个变量，它的值应该以逗号分隔的序列输入到程序中。
# 例子假设程序的输入序列是逗号分隔的:100，150，180，
# 程序输出为:18，22，24
# 提示:如果接收到的输出是小数，则应四舍五入到其最近的值(例如，如果接收到的输出是26.0，则应打印为26)。在为问题提供输入数据的情况下，应该假设它是控制台输入。
import math
c = 50
h = 30
value = []
print('请输入一组数字：')
items = [x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2 * c * float(d) / h)))))
print(','.join(value))