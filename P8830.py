def main():
    n = int(input())
    score = list(map(int, input().split()))
    sc = sorted(score[:2])
    max1 = sc[1]
    min1 = sc[0]
    sum1 = max1 + min1
    count1 = 0
    for i in score[2:]:
        if i > max1:
            max1 = i
        elif i < min1:
            min1 = i
        sum1 += i
        count1 += 1
        tmp = (sum1 - max1 - min1) / count1
        print('%.2f' % tmp)


if __name__ == '__main__':
    main()
