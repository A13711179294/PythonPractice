def printInfo(name,height,weight,hobby,pro):
    '''
    :param name:
    :param height:
    :param weight:
    :param hobby:
    :param pro:
    :return:
    '''
    print('%s的身高是%f,体重是%f,爱好是%s,职业是%s'%(name,height,weight,hobby,pro))
    pass
printInfo('ss',200,150,'play game','student')
def test1(a=10,b=20): #默认参数
    print('%d'%(a+b))
    pass
test1()
def test2(*args):
    result=0
    for item in args:
        result+=item
        pass
    print(result)
    pass
test2(1)
test2(1,2)