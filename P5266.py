dic = {}
for _ in range(int(input())):
    t = list(input().split())
    if len(t) == 3:
        dic[t[1]] = t[2]
        print('OK')
    elif len(t) == 2:
        if t[0] == '2':
            if t[1] in dic:
                print(dic[t[1]])
            else:
                print('Not found')
        else:
            if t[1] in dic:
                dic.pop(t[1])
                print('Deleted successfully')
            else:
                print('Not found')
    else:
        print(len(dic))