n = int(input())
end = n
digit = []
while end != 1:
    if end % 2 != 0:
        end = end * 3 + 1
        digit.append(end)
    else:
        end //= 2
        digit.append(end)
for i in digit[::-1]:
    print(i, end=' ')
print(n)
