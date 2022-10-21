# 编写程序，生成包含20个随机数的列表，然后将前10个元素升序排列，后10个元素降序排列，并输出结果。
import random

list1 = [random.randint(0,50) for i in range(20)]
print(list1)
list2 = list1[0:10]
list2.sort()
list1[0:10]=list2
list3 = list1[10:20]
list3.sort(reverse=True)
list1[10:20]=list3
print(list1)