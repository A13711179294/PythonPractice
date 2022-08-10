class Animal:
    def __eat(self):
        print('吃东西')
        pass
    def run(self):
        self.__eat()
        print('跑步')
        pass
class Bird(Animal):
    pass
b1=Bird()
# b1.eat()
b1.run()