import random
person=int(input('请出拳：[0：石头 1：剪刀 2：布]'))
computer=random.randint(0,2)
if person==0 and computer==1:
    print("你赢了")
    pass
elif person==1 and computer==2:
    print("你赢了")
    pass
elif person==2 and computer==0:
    print("你赢了")
    pass
elif person==computer:
    print("平局")
    pass
else:
    print("你输了")