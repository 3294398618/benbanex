# 文件的写入/写入了三行txt文本并关闭了文件
from sys import argv
# 读取了所操作文件的名称
script, filename = argv

print(f"We're going to  erase {filename}.")
# 后面两行无用仅流程
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# 用户确认
input("?")
# 表状态在打开
print("Opening the file...")
# 用
target = open(filename, "w")

print("Truncating the file. goodbye!")
target.truncate()

print("Now i'm going to ask you for three lines.")
# 得到123行
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# 文件写入操作
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3) # 尴尬line抄错了
target.write("\n")
# 一定要关掉！！！！
print("And finally,we close it.")
target.close()