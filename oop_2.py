class Pepole:
    def __init__(self,name,sex,age):
        '''
        实例属性的声明
        '''
        self.name=name
        self.sex=sex
        self.age=age
        pass
    def eat(self,food):
        print(self.name+"喜欢吃"+food)
        pass
    pass
sss=Pepole('sss','man','20')
xm=Pepole('xm','man','19')
print(sss.name,xm.name)
sss.eat('apple')