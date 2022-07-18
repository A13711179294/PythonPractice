#写函数，接受n个数字，求这些参数数字的和
def sumFunc(*args):
    result=0
    for item in args:
        result+=item
        pass
    return result
    pass
ret=sumFunc(1,2,3,4)
print("result=%d"%ret)
print('result=%d'%sumFunc(1,2))
print('result={}'.format(sumFunc(1,2,3,4,5,6,7,8,9,10)))