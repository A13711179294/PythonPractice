#求三组连续自然数的和：求出1到10、20到30、35到45的三个和
def sumRange(m,n):
    '''
    求从m到n的连续自然数的总和
    :param m: 
    :param n: 
    :return: 
    '''
    return sum(range(m,n+1))
    pass
print(sumRange(1,10))
print(sumRange(20,30))
print(sumRange(35,45))
