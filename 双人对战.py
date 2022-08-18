import time
import random
class Role:
    def __init__(self,name,hp):
        '''
        构造初始化函数
        :param name:角色名
        :param hp:血量
        '''
        self.name=name
        self.hp=hp
        pass
    def tong(self,enemy):
        enemy.hp-=15
        if enemy.hp < 0:
            enemy.hp = 0
        info='[%s]捅了[%s]一刀'%(self.name,enemy.name)
        print(info)
        pass
    def kan(self,enemy):
        enemy.hp -= 25
        if enemy.hp < 0:
            enemy.hp = 0
        info = '[%s]砍了[%s]一刀' % (self.name, enemy.name)
        print(info)
        pass
    def buxue(self):
        self.hp+=10
        if self.hp > 100:
            self.hp = 100
            pass
        info='[%s]吃了一颗补血药，增加10滴血'%(self.name)
        print(info)
        pass
    def miss(self):
        info = '[%s]进行了躲避' % (self.name)
        print(info)
        pass
    def __str__(self):
        return '[%s]的血量为[%s] '%(self.name,self.hp)
        pass
def control(pA,chooseA,chooseB,pB):
    if chooseA == 1 and chooseB != 4:
        pA.tong(pB)
        pass
    elif chooseA == 2 and chooseB != 4:
        pA.kan(pB)
        pass
    elif chooseA == 3 and chooseB != 4:
        pA.buxue()
        pass
    elif chooseA != 4 and chooseB == 4:
        pB.miss()
        print('[%s]进行了攻击，但是被[%s]躲开了'%(pA.name,pB.name))
        pass
player1=Role("player1",100)
player2=Role("player2",100)
while True:
    p1=random.randint(1,4)
    p2=random.randint(1,4)
    if(p1==p2==4):
        player1.miss()
        player2.miss()
        print('双方都进行了躲避')
    else:
        control(player1,p1,p2,player2)#玩家1的选择
        control(player2,p2,p1,player1)#玩家2的选择
    if player1.hp <= 0 and player2.hp > 0:
        print(player1, player2)
        print('游戏结束,play2胜利')
        break
    elif player1.hp > 0 and player2.hp <= 0:
        print(player1, player2)
        print('游戏结束,play1胜利')
        break
    elif player1.hp <= 0 and player2.hp <= 0:
        print(player1, player2)
        print('游戏结束,play1、play2同归于尽')
        break
    print(player1, player2)
    time.sleep(1)
    print('---------------------------------------------')
    pass