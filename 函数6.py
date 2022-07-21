#写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，并且将新内容返回给调用者
#PS：字典中的value只能是字符串或者列表
def dictFunc(dictParms):
    '''
    处理字典类型
    :param args:字典
    :return:字典
    '''
    result={}
    for key,value in dictParms.items():#key-value
        if len(value)>2:
            result[key]=value[:2]
        pass
    return result
    pass
dictObj={'name':'sss','pro':'computer','hobby':['唱歌','跳舞','Rap']}
ret=dictFunc(dictObj)
print(ret)