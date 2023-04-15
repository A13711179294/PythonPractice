s = input()
left = 0
right = 0
for i in range(len(s)):
    if s[i] == '.':
        left = ''.join(s[i - 1::-1]).lstrip('0')
        if left == '':
            left = '0'
        right = ''.join(s[:i:- 1]).rstrip('0')
        if right == '':
            right = '0'
        print(left + s[i] + right)
        break
    elif s[i] == '/':
        left = ''.join(s[i - 1::-1]).lstrip('0')
        if left == '':
            left = '0'
        right = ''.join(s[:i:- 1]).lstrip('0')
        print(left + s[i] + right)
        break
    elif s[i] == '%':
        left = ''.join(s[i - 1::-1]).lstrip('0')
        if left == '':
            left = '0'
        print(left + s[i])
        break
else:
    print(int(s[::-1]))
