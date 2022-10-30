#从键盘输入一个整数n，随机取自然数生成包含n个元素的列表，并打印输出。
from random import randint
num=int(input('请输入一个整数'))
listA=[randint(1,100) for i in range(0,num+1)]
print(listA)