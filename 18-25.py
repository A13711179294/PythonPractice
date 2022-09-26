# 题：网站要求用户输入用户名和密码进行注册。编写程序以检查用户输入的密码的有效性。
# 以下是检查密码的标准：
# 1. [a-z]之间至少有1个字母
# 2. [0-9]之间至少有1个数字
# 1. [A-Z]之间至少有一个字母
# 3. [$＃@]中至少有1个字符
# 4.最短交易密码长度：6
# 5.交易密码的最大长度：12
# 您的程序应接受一系列逗号分隔的密码，并将根据上述标准进行检查。将打印符合条件的密码，每个密码用逗号分隔。
# 例：如果以下密码作为程序的输入：
#
# ABd1234@1,a F1#,2w3E*,2We3345
# 然后，程序的输出应该是：
#
# ABd1234 @ 1
#
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。

import re
value = []
print("请输入：")
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print (",".join(value))