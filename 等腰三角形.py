row=1
while row<=5:
    j=1
    while j<=5-row:#控制打印空格的数量
        print(' ',end='')
        j+=1
        pass
    k=1
    while k<=2*row-1:#控制打印*号
        print('*',end='')
        k+=1
        pass
    print()
    row+=1