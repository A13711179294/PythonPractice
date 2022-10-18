#编写程序，生成包含1000个0到100之间的随机整数，并统计每个元素的出现次数。
from random import choice
from string import digits
z=''.join(choice(digits) for i in range(1000))
result={}
for ch in z:
    result[ch]=result.get(ch,0)+1
for digits,fre in sorted(result.items()):
    print(digits,fre,sep=':')