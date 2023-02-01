n = int(input().strip())
a = list(map(int, input().strip().split()))
ans = ''
for i in range(len(a)):
    if a[i] == -1:
        if n - i != 0 and n - i != 1:
            ans += '-' + 'x^' + str(n - i)
        elif n - i == 1:
            ans += '-' + 'x'
        else:
            ans += '-1'
    elif a[i] == 1:
        if n - i != 0 and n - i != 1:
            ans += '+' + 'x^' + str(n - i)
        elif n - i == 1:
            ans += '+' + 'x'
        else:
            ans += '+1'
    elif a[i] == 0:
        ans += ''
    else:
        if n - i != 0 and n - i != 1:
            if str(a[i])[0] == '-':
                ans += str(a[i]) + 'x^' + str(n - i)
            else:
                ans += '+' + str(a[i]) + 'x^' + str(n - i)
        elif n - i == 1:
            if str(a[i])[0] == '-':
                ans += str(a[i]) + 'x'
            else:
                ans += '+' + str(a[i]) + 'x'
        else:
            if str(a[i])[0] == '-':
                ans += str(a[i])
            else:
                ans += '+' + str(a[i])

print(ans.lstrip('+'))
