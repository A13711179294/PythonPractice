money_list = []

while len(money_list) < 12:
    temp = input().split()
    temp = [int(i) for i in temp]
    for i in temp:
        money_list.append(i)

flag = 0
save_money = 0
remain_money = 300 - money_list[0]  # 第一个月剩余的钱
for i in range(1, 12):
    temp = remain_money + 300 - money_list[i]  # 剩下的每个月的剩余的钱
    if temp < 0:
        flag = 1
        print('-%d' % (i + 1))
        break
    elif temp < 100:
        remain_money = temp
        pass
    else:
        save_money += (temp // 100) * 100
        remain_money = temp - (temp // 100) * 100
        pass
if flag == 0:
    if save_money * 0.2 + save_money + remain_money == int(save_money * 0.2 + save_money + remain_money):
        print(int(save_money * 0.2 + save_money + remain_money))
    else:
        print(save_money * 0.2 + save_money + remain_money)
