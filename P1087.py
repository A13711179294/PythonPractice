def FBI_tree(li):
    if len(li) > 1:
        FBI_tree(li[0:len(li) // 2])
        FBI_tree(li[len(li) // 2:])
        if '0' in li and '1' in li:
            print('F', end='')
        elif '0' in li and '1' not in li:
            print('B', end='')
        elif '0' not in li and '1' in li:
            print('I', end='')
    else:
        if '0' in li and '1' in li:
            print('F', end='')
        elif '0' in li and '1' not in li:
            print('B', end='')
        elif '0' not in li and '1' in li:
            print('I', end='')


N = int(input().strip())
s = list(input().strip())
FBI_tree(s)
