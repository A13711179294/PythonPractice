# 已知列表li_num1=[4,5,2,7]和li_num2=[3,6],
# 请编程将这个两个列表合并为一个列表，
# 并将合并后的列表中的元素从大到小的顺序排序。
li_num1=[4,5,2,7]
li_num2=[3,6]
li_new=li_num1+li_num2
li_new.sort(reverse=True)
print(li_new)