class Person:
    def eat(self):
        '''
        实例方法
        :return:
        '''
        print('self=%s',id(self))
        pass
    pass
xm=Person()
print('xm=%s',id(xm))
xm.eat()
class Animal:
    def __init__(self,name):
        self.name=name
        print('这是构造初始化的方法')
        pass
    def __del__(self):
        print('这是析构方法')
        pass
    pass
cat=Animal('xiaohua')