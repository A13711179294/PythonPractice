digit = set()
for i in range(10):
    digit.add(int(input()) % 42)
print(len(digit))