# s = list(input().strip())
# l = len(s) - 1
# li = ['0'] * 203
# s += ['0'] * (202 - l)
#
# i = 0
# while s[i] == '9':
#     i += 1
#     if i == l + 1:
#         s[0] = '1'
#         l += 1
#         while i > 0:
#             s[i] = '0'
#             i -= 1
#
# i = 0
# while i <= l - i:
#     li[i] = li[l - i] = s[i]
#     i += 1
#
# if li <= s:
#     i -= 1
#     while li[i] == '9':
#         i -= 1
#
#     li[i] = li[l - i] = str(int(li[i]) + 1)
#
#     i += 1
#     while i <= l - i:
#         li[i] = li[l - i] = '0'
#         i += 1
#
# print(*li[:l + 1], sep='')

s = input().strip()

if s.count('9') == len(s):
    s = '1' + '0' * len(s)

l = len(s)
t1 = s[:l // 2]
t2 = ''.join(list(reversed(t1)))

if l % 2 != 0:
    mid = s[l // 2]
    while True:
        tmp_num = t1 + mid + t2
        if int(tmp_num) > int(s):
            print(tmp_num)
            break
        if mid != '9':
            mid = str(int(mid) + 1)
            t1 = str(int(t1))
            t2 = ''.join(list(reversed(t1)))
        else:
            mid = '0'
            t1 = str(int(t1) + 1)
            if t1[-1] != '0':
                t2 = ''.join(list(reversed(t1)))
            else:
                t2 = ''.join(list(reversed(t1[0:-1])))

else:
    while True:
        tmp_num = t1 + t2
        if int(tmp_num) > int(s):
            print(tmp_num)
            break
        t1 = str(int(t1) + 1)
        t2 = ''.join(list(reversed(t1)))