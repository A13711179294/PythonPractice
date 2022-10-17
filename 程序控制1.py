a = []

for i in range(2,10):

    count = 0

    for x in range(2,i-1):

        if i % x == 0:

            count += 1

    if count != 0:

        a.append(i)

print(a)