x_dict = {}
y_dict = {}

for i in range(3):
    x, y = map(int, input().split())
    if x not in x_dict.keys():
        x_dict[x] = 1
    else:
        x_dict[x] += 1
    if y not in y_dict.keys():
        y_dict[y] = 1
    else:
        y_dict[y] += 1

print(min(x_dict, key=x_dict.get), min(y_dict, key=y_dict.get))
