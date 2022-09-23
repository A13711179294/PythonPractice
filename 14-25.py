# 题：编写一个接受句子的程序，并计算大写字母和小写字母的数量。
# 假设为程序提供了以下输入：
# Hello world!
# 然后，输出应该是：
# 大写实例 1
# 小写实例 9
#
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。

print('请输入：')
s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print ("UPPER CASE", d["UPPER CASE"])
print ("LOWER CASE", d["LOWER CASE"])