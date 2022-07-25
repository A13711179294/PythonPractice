M=lambda x,y:x+y
print(M(20,40))
result=lambda a,b,c:a*b*c
print(result(43,31,66))
test=lambda x,y:x if x>y else y
print(test(20,40))
rs=(lambda x,y:x if x>y else y)(30,10)
print(rs)
varRs=lambda x:(x**2)+890
print(varRs(10))