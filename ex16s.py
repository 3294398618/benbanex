from sys import argv
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

line1 = input("lines 1: ")
line2 = input("lines 2: ")
line3 = input("lines 3: ")

print("i'm going to write these to the file.")

target.write(lien1"\n"line2"\n"line3"\n")

print("and finally, we cloes it.")
target.close()