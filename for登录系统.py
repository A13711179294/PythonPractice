account='sss'
password='12345'
for i in range(3):
    ac=input('请输入账号:')
    pw=input('请输入密码:')
    if account==ac and password==pw:
        print('登陆成功...')
        break
        pass
    pass
else:
    print('你的账户已被锁定')