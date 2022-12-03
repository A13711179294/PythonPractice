n, k = map(int, input().split())

# new_count = n
# old_count = 0
# smoking_count = 0
#
# while new_count > 0:
#     new_count -= 1
#     old_count += 1
#     smoking_count += 1
#     if old_count == k:
#         new_count += 1
#         old_count = 0
#     if new_count == 0 and old_count < k:
#         break
#
# print(smoking_count)

print(n + (n - 1) // (k - 1))
