class Animal:
    '''
    父类【基类】
    '''
    def say_who(self):
        print('我是一个动物')
        pass
    pass
class Duck(Animal):
    '''
    子类【派生类】
    '''
    def say_who(self):
        print('我是鸭子')
        pass
    pass
class Dog(Animal):
    '''
    子类【派生类】
    '''
    def say_who(self):
        print('我是狗')
        pass
    pass
class Bird(Animal):
    def say_who(self):
        print('我是鸟')
        pass
    pass
class People:
    def say_who(self):
        print('我是人类')
        pass
    pass
class Student(People):
    def say_who(self):
        print('我是学生')
        pass
    pass
def commonInvoke(obj):
    '''
    统一调用方法
    :param obj:对象的实例
    :return:
    '''
    obj.say_who()

# duck1=Duck()
# duck1.say_who()
# dog1=Dog()
# dog1.say_who()

listObj=[Duck(),Dog(),Bird(),Student()]
for item in listObj:
    '''
    循环调用函数
    '''
    commonInvoke(item)