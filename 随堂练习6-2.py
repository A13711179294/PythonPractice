# 对于不规范的文本可以使用切片和字符串方法进行调整和规范化，规范化如下字符串：参考P74
# information=[‘姓名:张三’,’年龄：39’,’性别男’,’职业学生’,’籍贯：地球’]

information=['姓名:张三','年龄:39','性别男','职业学生','籍贯:地球']
for item in information :
    print(item[:2],item[2:].strip(': '),sep=': ')