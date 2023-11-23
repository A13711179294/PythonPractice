n = list(map(int, input().split()))
n.sort()
A = n[0]
B = n[1]
C = n[2]

if A + B > C and C - B < A:
    if A * A + B * B == C * C:
        print('Right triangle')
    if B * B + C * C < A * A or B * B + A * A < C * C or A * A + C * C < B * B:
        print('Obtuse triangle')
    if B * B + C * C > A * A and B * B + A * A > C * C and A * A + C * C > B * B:
        print('Acute triangle')
    if (A == B != C or A != B == C or A == C != B) or A == B == C:
        print('Isosceles triangle')
    if A == B == C:
        print('Equilateral triangle')
else:
    print('Not triangle')
