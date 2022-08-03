class shenxian:
    def fly(self):
        print("神仙都会飞")
        pass
class Monkey:
    def EatPeach(self):
        print('猴子喜欢吃桃')
        pass
class SunWuKong(shenxian,Monkey):
    pass
swk=SunWuKong()
swk.EatPeach()
swk.fly()