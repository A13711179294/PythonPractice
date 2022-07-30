#指定一个列表，列表里含有唯一一个只出现过一次的数字，写程序找出这个“独一无二”的数字
li=[1,2,2,3,3,4,4,5,5,6,6,7,7]
set1=set(li)
for i in set1:
    li.remove(i)
    pass
set2=set(li)
for i in set1:
    if i not in set2:
        print(i)
        pass
    pass
pass