# 问题:编写一个程序，接受一系列空格分隔的单词作为输入，并在删除所有重复的单词并按字母数字排序后打印这些单词。
# 假设向程序提供以下输入:
# hello world and practice makes perfect and hello world again
# 则输出为:
# again and hello makes perfect practice world
# 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。
# 我们使用set容器自动删除重复的数据，然后使用sort()对数据进行排序。
print('请输入一组字符串：')
s = input()
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))