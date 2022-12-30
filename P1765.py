str1 = input()
count = 0
for i in str1:
    if i in 'adgjmptw ':
        count += 1
    if i in 'behknqux':
        count += 2
    if i in 'cfilorvy':
        count += 3
    if i in 'sz':
        count += 4
print(count)
