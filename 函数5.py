#写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
def process_Func(con):
    listNew=[]
    index=1
    for i in con:
        if index%2==1:
            listNew.append(i)
            pass
        index+=1
        pass
    return listNew
    pass
listA=[0,2,3,4,5,6,8,9,10,63]
ret1=process_Func(listA)
print(ret1)
ret2=process_Func(tuple(range(10,30)))
print(ret2)