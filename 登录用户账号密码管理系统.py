dict1 = user = {'Wangwu': 123456, 'Zhangsan': 456789, 'Lisi': 789123}


def menu():
    print('+++++++++++欢迎使用用户管理系统+++++++++++++')
    print('1.显示已有帐号和密码')
    print('2.添加新用户账号和密码')
    print('3.删除无效用户账户和密码')
    print('4.查询账号对应密码')
    print('5.修改密码')
    print('0.退出系统')
    print('+++++++++++++++++++++++++++++++++++++++++')


x = 1
while x != 0:
    menu()
    x = int(input('请输入你要进行的操作(0-5):'))
    if x == 1:
        for key, value in dict1.items():
            print('账号：%s:密码：%s' % (key, value))
    elif x == 2:
        try:
            account = input('请输入账号：')
            password = int(input('请输入密码：'))
            dict1[account] = password
        except:
            print('添加失败')
        else:
            print('添加成功')
    elif x == 3:
        try:
            account = input('请输入删除账号：')
            dict1.pop(account)
        except:
            print('删除失败')
        else:
            print('删除成功')
    elif x == 4:
        try:
            account = input('请输入查询账号：')
            print(dict1[account])
        except:
            print('查询失败')
        else:
            print('查询成功')
    elif x == 5:
        account = input('请输入修改账号：')
        if account in dict1.keys():
            print('账号：%s:密码：%s' % (account, dict1[account]))
            password = int(input('请输入新密码：'))
            dict1[account] = password
            print('修改成功')
        else:
            print('账号不存在')
            print('修改失败')
    elif x == 0:
        pass
    else:
        print('输入错误')