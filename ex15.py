# 打开文件
from sys import argv

script, filename = argv
# 现在txt代表了文件
txt = open(filename)

print(f"Here's your file {filename}:")
# 开txt（文件）
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())