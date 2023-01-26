class People:
    def __init__(self, name = None , phone = None):
        self.name = name
        self.phone = phone
    def __str__(self):
        return '好友姓名：' + self.name + '好友手机号：' + self.phone

def menu():
    print('欢迎使用好友管理系统')
    print('1:添加好友')
    print('2:删除好友')
    print('3:修改好友')
    print('4：展示好友')
    print('5:退出')

address = []

while True:
    menu()
    choose = int(input())
    if choose == 1:
        print('请输入姓名')
        name = input()
        print('请输入手机号')
        phone = input()
        address.append(People(name, phone))
        print('添加成功')
    elif choose == 2:
        print('请输入姓名')
        tmp_name = input()
        for i in address:
            if tmp_name == i.name:
                address.remove(i)
                print('删除成功')
                break
        else:
            print('找不到该好友')
    elif choose == 3:
        print('请输入需要修改的好友的姓名')
        tmp_name = input()
        for i in address:
            if tmp_name == i.name:
                print('请输入修改后的姓名')
                modify_name = input()
                i.name = modify_name
                print('请输入修改后的手机号')
                modify_phone = input()
                i.name = modify_phone
                print('修改成功')
                break
        else:
            print('找不到该好友')
    elif choose == 4:
        for i in address:
            print(i.__str__())
    elif choose == 5:
        print('成功退出')
        break
    else:
        print('输入错误，请重新输入')
