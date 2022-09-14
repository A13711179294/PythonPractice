import math
"""
根据身高体重计算某个人的BMI指数:
体质指数（BMI）=体重（kg）÷身高^2（m）
"""
weight,height=map(float,input('请输入体重（kg）和体重（m）(中间用空格隔开):').split())
BMI=weight/math.pow(height,2)
print('您的体质指数（BMI）为%f'%BMI)