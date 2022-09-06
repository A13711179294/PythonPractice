import re
res1=re.match('[A-Z][A-Z]*','My111') #*匹配前一个字符出现0次或者无限次，即可有可无
print(res1.group())
res2=re.match('[a-zA-Z]+','aW1234e') #匹配前一个字符出现1次或者无限次，至少有1次
print(res2.group())
res3=re.match('[a-zA-Z_]+[\w]*','n13ame') #匹配符合规则
print(res3.group())
res4=re.match('[a-zA-Z][0-9]?','n12ame') #匹配0次或1次
print(res4.group())
res5=re.match('\d{4}','1234567890')
if res5:
    print('匹配成功{}'.format(res5.group()))
res5=re.match('\d{4,}','1234567890')
if res5:
    print('匹配成功{}'.format(res5.group()))
res5 = re.match('\d{4,7}', '1234567890')
if res5:
    print('匹配成功{}'.format(res5.group()))
regexMail=re.match('[a-zA-Z0-9]{6,11}@qq.com','abcd12345@qq.com')
print(regexMail.group())