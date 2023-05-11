dic = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
       "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
       "eighteen": 18, "nineteen": 19, "twenty": 20,
       "a": 1, "both": 2, "another": 1, "first": 1, "second": 2, "third": 3}
li = list(input().split())
s = []
for i in li:
    if i in dic:
        tmp = dic[i] * dic[i] % 100
        if tmp == 0:
            continue
        s.append(tmp)

if s:
    s.sort(key=lambda x: x)
    print(s[0], end='')
    for i in range(1, len(s)):
        if s[i] < 10:
            print(0, end='')
        print(s[i], end='')
else:
    print(0)
