import time
class TimeTest:
    def __init__(self,hour,min,second):
        self.hour=hour
        self.min=min
        self.second=second
    @staticmethod
    def showtime():
        return time.strftime("%H:%M:%S",time.localtime())
        pass
    pass
print(TimeTest.showtime())
# t=TimeTest(2,10,15)
# print(t.showtime())#没有必要用这种方法去访问 静态方法