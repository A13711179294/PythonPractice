s = input()

stack = []
sum = 0
tmp = ''
for i in s:
    if i.isdigit():
        tmp += i
    elif i == '.':
        stack.append(int(tmp))
        tmp = ''
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        sum = b - a
        stack.append(sum)
    elif i == '+':
        a = stack.pop()
        b = stack.pop()
        sum = b + a
        stack.append(sum)
    elif i == '*':
        a = stack.pop()
        b = stack.pop()
        sum = b * a
        stack.append(sum)
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        sum = b // a
        stack.append(sum)
    elif i == '@':
        break

print(sum)

