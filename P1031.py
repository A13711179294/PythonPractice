N = int(input())
sum1 = 0
card = list(map(int, input().split()))
average = sum(card) // N
count1 = 0

for i in range(N - 1):
    if card[i] < average:
        card[i + 1] = card[i + 1] - (average - card[i])
        card[i] = average
        count1 += 1
    elif card[i] > average:
        card[i + 1] = card[i + 1] + (card[i] - average)
        card[i] = average
        count1 += 1

print(count1)
