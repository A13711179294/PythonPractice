def add(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 > l2:
        c = l1 - l2
        for _ in range(c):
            S2.insert(0, 0)
    elif l1 < l2:
        c = l2 - l1
        for _ in range(c):
            S1.insert(0, 0)


prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
S1, S2 = input().split('+')
S1 = list(map(int, S1.split(',')))
S2 = list(map(int, S2.split(',')))
add(S1, S2)
ans = []
j = 0
for i in range(len(S1) - 1, -1, -1):
    tmp = S1[i] + S2[i]
    if tmp >= prime[j]:
        t1 = tmp % prime[j]
        t2 = tmp // prime[j]
        tmp = t1
        ans.append(t1)
        if i - 1 < 0:
            ans.append(t2)
        else:
            S1[i - 1] += t2
    else:
        ans.append(tmp)
    j += 1

ans.reverse()
for i in range(len(ans)):
    ans[i] = str(ans[i])
print(','.join(ans))

