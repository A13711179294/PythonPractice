class Person:
    '''
    对应人的特征
    '''
    age=20 #类属性
    '''
    对应人的行为
    '''
    def __init__(self):
        self.name='xxx' #实例属性
        pass
    def eat(self): #实例方法
        print("大口的吃饭")
        pass
    def run(self): #实例方法
        print("快速的奔跑")
        pass
xm=Person()
xm.eat() #调用函数
xm.run() #调用函数
print('{} {}'.format(xm.name,xm.age))
