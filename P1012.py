n = int(input())
ai = list(input().split())
ai.sort(reverse=True)

for i in range(0, n - 1):
    if int(ai[i] + ai[i + 1]) < int(ai[i + 1] + ai[i]):
        ai[i], ai[i + 1] = ai[i + 1], ai[i]

for i in ai:
    print(i, end='')
