s = list(input().strip())
stack = []
b = [' '] * 101
for i in range(len(s)):
    if s[i] == '[':
        stack.append(i)
        b[i] = ']'
    elif s[i] == '(':
        stack.append(i)
        b[i] = ')'
    else:
        if not stack or b[stack[-1]] != s[i]:
            if s[i] == ')':
                b[i] = '('
            else:
                b[i] = '['
        else:
            id = stack[-1]
            stack.pop()
            b[id] = ' '

# print(s)
# print(b)
for i in range(len(s)):
    if b[i] == '(' or b[i] == '[':
        print(b[i], end='')
    print(s[i], end='')
    if b[i] == ')' or b[i] == ']':
        print(b[i], end='')
