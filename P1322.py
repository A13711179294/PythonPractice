# from sys import setrecursionlimit
#
# setrecursionlimit(10000)
#
#
# def dfs():
#     global i, l
#     sum1 = 0
#     while i < l:
#         if s[i] == 'F':
#             i += 3
#             tmp = ''
#             while i < l and s[i] != ' ':
#                 tmp += s[i]
#                 i += 1
#                 if s[i] == ']':
#                     sum1 += int(tmp)
#                     i += 1
#                     return sum1
#             sum1 += int(tmp)
#             i += 1
#         elif s[i] == 'B':
#             i += 3
#             tmp = ''
#             while i < l and s[i] != ' ':
#                 tmp += s[i]
#                 i += 1
#                 if s[i] == ']':
#                     sum1 -= int(tmp)
#                     i += 1
#                     return sum1
#             sum1 -= int(tmp)
#             i += 1
#         elif s[i] == 'R':
#             i += 7
#             tmp = ''
#             while s[i] != '[':
#                 tmp += s[i]
#                 i += 1
#             i += 1
#             sum1 += int(tmp) * dfs()
#         elif s[i] == ']':
#             i += 1
#             return sum1
#
#
# s = list(input()) + [']']
# i = 0
# l = len(s)
# print(abs(dfs()))

print(abs(eval(input().replace(' ', '').replace('FD', '+').replace('BK', '-').replace('REPEAT', '+(').replace('[', ')*(').replace(']', ")").replace('()','0'))))
