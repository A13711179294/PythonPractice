class ToolongMyException(Exception):
    def __init__(self,len):
        self.len=len
        pass
    def __str__(self):
        return "您输入的数据长度是"+str(self.len)+'超过长度了...'
def name_Test():
    name=input("请输入姓名......")
    try:
        if len(name)>4:
            raise ToolongMyException(len(name))
        else:
            print(name)
    except ToolongMyException as msg:
        print(msg)
name_Test()