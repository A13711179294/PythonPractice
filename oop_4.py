class Pepole:
    def __init__(self,name,sex,age,pro,food):
        '''
        :param name: 姓名
        :param sex:性别
        :param age:年龄
        :param pro:职业
        :param food:食物
        '''
        self.name=name
        self.sex=sex
        self.age=age
        self.pro=pro
        self.food=food
        print('__init__函数的执行')
        pass
    def __str__(self):
        '''
        打印对象 自定义对象 是格式内容的
        :return:
        '''
        return '%s喜欢吃%s'%(self.name,self.food)
        pass
    def __new__(cls, *args, **kwargs):
        '''
        创建对象实例的方法 每调用一次 就会生成一个新的对象
        cls就是class的缩写
        :param args:
        :param kwargs:
        '''
        print('__new__函数的执行')
        return object.__new__(cls)#在这里是真正创建对象实例的
        pass
    pass
xw=Pepole('xw','man',20,'computer','banana')
print(xw)