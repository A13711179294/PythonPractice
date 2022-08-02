class Animal:
    def eat(self):
        print('吃饭')
        pass
    def drink(self):
        print('喝水')
        pass
    pass
class Dog(Animal):#继承Animal 父类 此时Dog就是子类
    def brak(self):
        print('狗叫')
        pass
class Cat(Animal):
    def meow(self):
        print('猫叫')
        pass
d1=Dog()
c1=Cat()
d1.eat()
c1.drink()