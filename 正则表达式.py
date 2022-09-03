import re
strData = 'Python is the best language in the world'
#match 只能匹配以xxx开头的字符串，第一个参数是正则，第二个参数是需要匹配的字符串
res = re.match('p',strData,re.I|re.M) # 第三个参数 表示忽略大小写
if res:
    print('匹配成功')
    print(res)
    print(res.group())
else:
    print(res)
    print('匹配失败....')