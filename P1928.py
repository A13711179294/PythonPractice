def dfs():
    global i
    tmp = ''
    while i < len(s):
        if s[i] == '[':
            i += 1
            num = ''
            while s[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                num += s[i]
                i += 1
            tmp += int(num) * dfs()

        elif s[i] == ']':
            i += 1
            return tmp
        else:
            tmp += s[i]
            i += 1
    return tmp


s = list(input().strip())
i = 0
print(dfs())
