def bubble_sort(li, n):
    global count
    for i in range(1, n):
        flag = False
        for x in range(n - i):
            if li[x] > li[x + 1]:
                li[x], li[x + 1] = li[x + 1], li[x]
                flag = True
                count += 1
        if not flag:
            return


count = 0
N = int(input())
carriage_list = []

while len(carriage_list) < N:
    num = input()
    nums = num.strip().split()
    nums = [int(i) for i in nums]
    for i in nums:
        carriage_list.append(i)

bubble_sort(carriage_list, N)
print(count)
