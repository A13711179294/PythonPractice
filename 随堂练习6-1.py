# 编写程序：从键盘输入一个整数n，随机取自然数生成包含n个元素的列表。用切片取出：
# （1）列表的前5个元素；
# （2）列表的后5个元素；

from random import randint
num1=int(input('请输入一个整数'))
listA=[randint(1,100) for i in range(0,num1)]
print('前5个元素为{}'.format(listA[0:5]))
print('后5个元素为{}'.format(listA[:-6:-1]))