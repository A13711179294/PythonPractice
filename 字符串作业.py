# 获得输入的一个字符串s，以字符减号(-)分割s，将其中首尾两段用加号(+)组合后输出。
str=input('请输入一个字符串：').split('-')
strlist=[]
strlist.append(str[0])
strlist.append(str[-1])
print('+'.join(strlist))