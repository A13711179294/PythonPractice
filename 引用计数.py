import sys
a=[]
print(sys.getrefcount(a))
b=a
print(sys.getrefcount(a))
c=b
d=b
e=c
f=e
g=d
print(sys.getrefcount(a))