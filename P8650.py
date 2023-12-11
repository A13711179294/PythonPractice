def dfs():
    global pos, length
    ans, temp = 0, 0
    while pos < length:
        if s[pos] == '(':
            pos += 1
            temp += dfs()
        elif s[pos] == 'x':
            pos += 1
            temp += 1
        elif s[pos] == '|':
            pos += 1
            ans = max(ans, temp)
            temp = 0
        elif s[pos] == ')':
            pos += 1
            break

    ans = max(ans, temp)
    return ans


s = input().strip()
pos, length = 0, len(s)
ret = dfs()
print(ret)
