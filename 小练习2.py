#100个和尚吃100个馒头，大和尚一人吃3个馒头，小和尚三天吃一个馒头。请问大小和尚各多少人
def PersonCount():
    for a in range(1,101):
        if a*3+(100-a)*(1/3)==100:
            return (a,100-a)
        pass
    pass
ret=PersonCount()
print(ret[0],ret[1])