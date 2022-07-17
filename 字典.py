dictA={}
dictB={'pro':'computer','school':'ggs'}
dictA['name']='sss'
dictA['age']=20
dictA['pos']='student'
print(dictA)
print(dictA['name'])
print(dictB['pro'])
dictA['age']='22'
print(dictA['age'])
print(dictA.keys())
print(dictA.values())
print(dictA.items())
for item in dictA.items():
    print(item)
for key,value in dictA.items():
    print('%s==%s'%(key,value))
dictA.update({'height':177})
del dictA['name']
dictB.pop('pro')
sorted(dictA.items(),key=lambda d:d[0])