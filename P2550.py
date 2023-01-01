n = int(input())
RewardList = list(map(int, input().split()))

BuyList = []
RewardDict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for x in range(1, n + 1):
    ItemBuyList = list(map(int, input().split()))
    BuyList.append(ItemBuyList)

for y in range(0, n):
    count = 0
    for z in range(0, 7):
        if RewardList[z] in BuyList[y]:
            count += 1
    if count == 7:
        RewardDict[0] += 1
    elif count == 6:
        RewardDict[1] += 1
    elif count == 5:
        RewardDict[2] += 1
    elif count == 4:
        RewardDict[3] += 1
    elif count == 3:
        RewardDict[4] += 1
    elif count == 2:
        RewardDict[5] += 1
    elif count == 1:
        RewardDict[6] += 1

for value in RewardDict.values():
    print(value, end=' ')
