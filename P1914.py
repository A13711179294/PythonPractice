n = int(input())
s = [' '] + list(input())
for i in range(1, len(s)):
    print(chr(ord('a') + (ord(s[i]) + n - 97) % 26), end='')
