# def test1(n):
#     result=1
#     for item in range(1,n+1):
#         result*=item
#         pass
#     return result
#     pass
# print(test(5))
def test2(n):
    '''
    递归实现
    :param n: 阶乘参数
    :return:
    '''
    if n==1:
        return 1
    else:
        return n*test2(n-1)
    pass
print(test2(6))
#递归案例 模拟实现 树形结构的遍历
import os #引入文件操作模块
def findFile(flie_Path):
    listRs=os.listdir(flie_Path)  #得到该路径下所有的文件夹
    for fileItem in listRs:
        full_path=os.path.join(flie_Path,fileItem) #获取完整的文件路径
        if os.path.isdir(full_path):#判断是否是文件夹
            findFile(full_path)
        else:
            print(fileItem)
            pass
        pass
    else:
        return
    pass