class Person:
    def __init__(self):
        self.__age=18
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age=age
            pass
    age=property(get_age,set_age)
    pass
p1=Person()
print(p1.age)
p1.age=25
print(p1.age)