num,money=input('请输入需要充值的手机号与金额：(中间用空格隔开)').split()
money=int(money)
if(money>0):
    print('手机号：{}充值成功'.format(num))
else:
    print('充值的金额不能小于0')