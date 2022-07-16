#嵌套调用
def test1():
    print(1)
    pass
def test2():
    print(2)
    test1()
    pass
test2()