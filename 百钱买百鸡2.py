list1=[(x, y, 100-x-y) for x in range(21) for y in range(34) if(100-x-y)%3 ==0 and 5*x+3*y+(100-x-y)//3== 100]
print(list1)