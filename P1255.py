N = int(input())
step = [1, 2]
for i in range(2, N):
    step.append(step[i - 1] + step[i - 2])
print(step[N-1])
