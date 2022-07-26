a=1 #不可变类型
def test1(x):
    print('x的地址{}'.format(id(x)))
    x=2
    print('x的值修改后的地址{}'.format(id(x)))
    pass
print('x的地址{}'.format(id(a)))
test1(a)
print(a)

listA=[] #可变类型
def test2(parms):
    print(id(parms))
    listA.append([1,2,3,4,5,6,7,8,9,10])
    listA.append(11)
    pass
print(id(listA))
test2(listA)
print(listA)