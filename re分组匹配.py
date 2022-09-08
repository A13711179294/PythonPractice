import re
string='fsfsf222'
ret=re.match('(fsfsf|fsfsf222)',string)
print(ret.group())
htmlTag='<html><h1>测试数据</h1></html>'
res1=re.match(r'<(.+)><(.+)>(.+)</\2></\1>',htmlTag)
print(res1.group())
data='<div><h1>www.baidu.com</h1></div>'
res2=re.match(r'<(?P<div>\w*)><(?P<h1>\w+)>.*</(?P=h1)></(?P=div)>',data)
print(res2.group())
