import re
#贪婪模式
rs1=re.match('\d{6,9}','111222333')
print(rs1.group())

content='abcdacbc'

pattern1=re.compile('a.*b')
result=pattern1.search(content)
print('贪婪模式%s'%result.group())


#非贪婪模式
rs2=re.match('\d{6,9}','111222333')
print(rs2.group())

pattern2=re.compile('a.*?b')
result=pattern2.search(content)
print('非贪婪模式%s'%result.group())

