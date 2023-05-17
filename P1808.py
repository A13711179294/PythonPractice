N = int(input())
letter = set()
tmp = N
while tmp > 0:
    d = list(input())
    d.sort()
    d = ''.join(d)
    letter.add(d)
    tmp -= 1
print(len(letter))