def Sum(a,b):
    sum=a+b
    return sum
    pass
ret=Sum(10,30)
print(ret)
def calComputer(num):
    li=[]
    result=0
    i=1
    while i<=num:
        result+=i
        i+=1
        pass
    li.append(result)
    return li
    pass
print(calComputer(5))
def returnTuple():
    '''
    返回元组类型数据
    :return:
    '''
    return 1,2,3
    pass
A=returnTuple()
print(type(A))
def returndict():
    '''
    返回字典类型数据
    :return:
    '''
    return {"name":"sss"}
    pass
B=returndict()
print(type(B))