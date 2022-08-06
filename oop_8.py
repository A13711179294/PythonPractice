class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        pass
    def brak(self):
        print('狗叫')
        pass
    pass
class kejiquan(Dog):
    def __init__(self,name,color):#属于重写父类的方法
        Dog.__init__(self,name,color)#手动调用父类的方法
        #super.__init__(name,color)
        self.height=90
        self.weight=20
        pass
    def __str__(self):
        return "颜色{} 身高{} 体重{}".format(self.color,self.height,self.weight)
    def brak(self):#属于重写父类的方法
        super().brak() #super是自动找到父类 进而调用方法
        print('keji叫')
        pass
keji=kejiquan('柯基犬','白色')
print(keji)
keji.brak()