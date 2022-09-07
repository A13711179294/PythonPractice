import re
reobj=re.compile('\d{4}')
rs1=reobj.match('12345678')
print(rs1.group())

print(re.match('\d{4}','12345678').group())

data='1234ab cd567abcd890'
rs2=re.search('cd',data)
print(rs2)
print(rs2.group())

data2='华为是华人的骄傲'
rs=re.findall('华.' ,data2)
print(rs)

data3='Python是很受欢迎的编译语言'
pattern='[a-zA-Z]+'
res=re.sub(pattern,'C#',data3)
resn=re.subn(pattern,'C#',data3)
print(res)
print(resn)

data4='百度，腾讯，阿里，华为，360'
rs3=re.split(',',data4)
print(rs3)