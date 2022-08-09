class People:
    country='china'
    @classmethod
    def get_country(cls):
        return cls.country#访问类属性
    pass
    @classmethod
    def change_country(cls,data):
        cls.country=data#修改类属性的值 在类方法中
        pass
    @staticmethod
    def getData():
        return People.country
        pass
    @staticmethod
    def add(x,y):#带参数的静态方法
        return x+y
        pass
print(People.country)
p=People()
print(p.get_country())
People.change_country('Russia')
print(People.get_country())
print(People.getData())
print(People.add(3,5))