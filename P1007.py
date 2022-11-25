L = int(input().strip())
N = int(input().strip())
if N == 0:
    print(0, 0)
else:
    soldiers_list = list(map(int, input().strip().split()))
    max_index = []
    min_index = []
    for i in soldiers_list:
        left = i
        right = L + 1 - i
        if left > right:
            left, right = right, left
        max_index.append(left)
        min_index.append(right)
    print(max(max_index), end=' ')
    print(max(min_index))
