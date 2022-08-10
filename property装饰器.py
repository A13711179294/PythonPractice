class Person:
    def __init__(self):
        self.__age=18
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,parms):
        if parms < 0:
            print('年龄不能小于0')
        else:
            self.__age=parms
            pass
        pass
p1=Person()
print(p1.age)
p1.age=30
print(p1.age)
