import re
data='aaaaa'
names='李达','李明','小王','小李','小华'
str='hello'
datas='a','b','c','d','e','f'
pattern='李.' #匹配规则
parrtern='...' #匹配规则
pattern1='[a-z]' #简写一个范围
for name in names:
    res1=re.match(pattern,name)
    if res1:
        print(res1.group())
res2=re.match('[he]',str)
print(res2.group())
for item in datas:
    res3=re.match(pattern1,item)
    if res3:
        print(res3.group())
