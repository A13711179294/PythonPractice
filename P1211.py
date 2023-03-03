n = int(input())
a = list(input().split())

ans = 0
for i in range(100, 1000):
    for j in range(10, 100):
        if str(i)[0] in a and str(i)[1] in a and str(i)[2] in a and str(j)[0] in a and str(j)[1] in a:
            if len(str(int(str(j)[1]) * i)) == 3 and len(str(int(str(j)[0]) * i)) == 3:
                if str(int(str(j)[1]) * i)[0] in a and str(int(str(j)[1]) * i)[1] in a and str(int(str(j)[1]) * i)[
                    2] in a:
                    if str(int(str(j)[0]) * i)[0] in a and str(int(str(j)[0]) * i)[1] in a and str(int(str(j)[0]) * i)[
                        2] in a:
                        if len(str(int(str(j)[1]) * i + int(str(j)[0]) * i * 10)) == 4:
                            if str(int(str(j)[1]) * i + int(str(j)[0]) * i * 10)[0] in a and \
                                    str(int(str(j)[1]) * i + int(str(j)[0]) * i * 10)[1] in a and \
                                    str(int(str(j)[1]) * i + int(str(j)[0]) * i * 10)[2] in a and \
                                    str(int(str(j)[1]) * i + int(str(j)[0]) * i * 10)[3] in a:
                                ans += 1

print(ans)
