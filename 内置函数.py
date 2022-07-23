#取绝对值
print(abs(-34))
#取近似值
print(round(-3.4565,3))
#pow 求次方
print(3**3)
print(pow(3,3))
#divmod 求商和余数
print(divmod(7,3))
#max 求最大值
print(max([23,43,65563,323,12,54,87,76]))
#sum
print(sum(range(50),3))
#eval 执行表达式
a,b,c=1,2,3
print(eval('a+b+c'))
def test1():
    print(12345)
    pass
eval("test1()")
print(eval('d+e+f',{'e':4,'d':5,'f':6}))