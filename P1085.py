class_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

for i in range(1, 8):
    in_school, after_school = map(int, input().split())
    class_dict[i] = in_school + after_school

temp = 0
emo_max = 0

for i in range(1, 7):
    if 8 < class_dict[i]:
        if emo_max < class_dict[i]:
            emo_max = class_dict[i]
            temp = i

print(temp)
