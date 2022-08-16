class Student(object):
    __slots__ = ('name','age')
    def __str__(self):
        return '{}...{}'.format(self.name,self.age)
    pass

xw=Student()
xw.name='xw'
xw.age=20
# xw.score=90 没有在范围内所以报错
# print(xw.__dict__) #所有可用的属性都存储在这 不足的地方就是占用的内存空间大
print(xw)

class subStudent(Student):
    # __slots__ = () #子类声明了__slots__时 继承父类的__slots__，也就是子类的范围为自身+父类的
    pass
xh=subStudent()
xh.name='xh'
xh.age=21
xh.pro='computer'
xh.score=95
print(xh)