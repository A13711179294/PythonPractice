# from queue import PriorityQueue
#
#
# def main():
#     k, m = map(int, input().split())
#     q = PriorityQueue()
#     q.put(1)
#     str1 = ''
#     for i in range(k):
#         p = q.get()
#         str1 += str(p)
#         q.put(2 * p + 1)
#         q.put(4 * p + 5)
#
#     li = list(map(int, str1))
#
#     stack = []
#     for j in li:
#         while stack and j > stack[-1] and m:
#             stack.pop()
#             m -= 1
#         stack.append(j)
#
#     print(*li, sep='')
#     print(*stack, sep='')
#
#
# main()


def main():
    k, m = map(int, input().split())
    tmp1 = 0
    tmp2 = 0
    S = [1]
    for i in range(k - 1):
        if S[tmp1] * 2 + 1 < S[tmp2] * 4 + 5:
            S.append(S[tmp1] * 2 + 1)
            tmp1 += 1
        else:
            S.append(S[tmp2] * 4 + 5)
            tmp2 += 1
    li = list(''.join(map(str, S)))

    stack = []
    for j in li:
        while stack and j > stack[-1] and m:
            stack.pop()
            m -= 1
        stack.append(j)
    while m:
        stack.pop()
        m -= 1
    print(*li, sep='')
    print(*stack, sep='')


main()