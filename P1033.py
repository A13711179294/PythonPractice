from math import sqrt

H, S1, V, L, K, n = map(float, input().split())
n = int(n)
t_max = sqrt(H / 5)
t_min = sqrt((H - K) / 5)
i_b = int(S1 - t_min * V + L)
i_e = int(S1 - t_max * V)
i_b = min(i_b, n)
i_e = max(i_e, 0)
print(i_b-i_e)
