letter_str = input().strip()

new_str = letter_str.replace('boy', '1').replace('girl', '2').replace('bo', '1').replace('oy', '1').replace('gir','2').replace('irl', '2').replace('rl', '2').replace('gi', '2').replace('ir', '2')

temp1 = new_str.count('1') + new_str.count('b') + new_str.count('o') + new_str.count('y')
temp2 = new_str.count('2') + new_str.count('g') + new_str.count('i') + new_str.count('r') + new_str.count('l')

print(temp1)
print(temp2)