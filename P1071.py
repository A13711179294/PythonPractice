message1 = list(input().strip())
message2 = list(input().strip())
message3 = input().strip()

password = dict(zip(message1, message2))
tuple1 = tuple(zip(message1, message2))
flag = 0

if len(set(password.keys())) < 26:
    print('Failed')
else:
    for i in range(len(tuple1)):
        if flag == 1:
            break
        for j in range(i, len(tuple1)):
            if tuple1[i][0] != tuple1[j][0] and tuple1[i][1] == tuple1[j][1]:
                print('Failed')
                flag = 1
                break
    else:
        try:
            result1 = []
            for i in message3:
                result1.append(password[i])
            print(''.join(result1))
        except:
            print('Failed')

# AAQWERTYUIOPLKJHGFDSAZXCVBNM
# ABQWERTYUIOPLKJHGFDSAZXCVBNM
# HELLO