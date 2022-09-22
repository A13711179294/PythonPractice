# 题：编写一个接受句子并计算字母和数字的程序。假设为程序提供了以下输入：
# Hello world! 123
# 然后，输出应该是：
# 字母10
# 数字3
#
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。

print('请输入：')
s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("LETTERS", d["LETTERS"])
print ("DIGITS", d["DIGITS"])