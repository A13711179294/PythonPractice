import re
data1='1335643789fsdafag'
data2='fsdaf42432ag'
data3='  hello'
data4='....'
print(re.match('\d\d',data1).group()) #匹配数字
print(re.match('\D',data2).group()) #匹配字母
print(re.match('\s',data3).group()) #匹配一个空白字符或者tab键
print(re.match('\S',data1).group()) #匹配非空白字符
print(re.match('\w',data1).group()) #匹配单词字符
print(re.match('\W',data4).group()) #匹配非单词字符