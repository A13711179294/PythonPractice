N = int(input())
num_list = map(int, input().split())
num_set = set(num_list)
num_count = len(num_set)
num_list = list(num_set)
num_list.sort()

num_list = map(str, num_list)

print(num_count)

print(' '.join(num_list))
