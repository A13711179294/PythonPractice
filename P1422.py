total = int(input())
if 0 <= total <= 150:
    money = total * 0.4463
elif 151 <= total <= 400:
    money = (total - 150) * 0.4663 + 150 * 0.4463
else:
    money = (total - 400) * 0.5663 + 250 * 0.4663 + 150 * 0.4463
print(round(money, 1))
