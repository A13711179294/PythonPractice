s, t, w = map(int, input().strip().split())
Jam_str = list(input().strip())

for i in range(1, 6):
    for j in range(w - 1, 0, -1):
        if ord(Jam_str[j]) - 96 <= j - w + t:
            Jam_str[j] = chr(ord(Jam_str[j]) + 1)
            for k in range(j + 1, w):
                Jam_str[k] = chr(ord(Jam_str[k - 1]) + 1)
            print(*Jam_str, sep='')
            break
