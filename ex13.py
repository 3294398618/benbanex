# 调用函数/sys可在程序开始的时候请求写入数据
from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv    # 逗号后面要空格  #前面4个 第1个表示项目名称 后三个为新建变量需要开始程序时提供常熟的    可改变变量数量

print("the script is called:", script)
print("your first variable is:", first)# 同上
print("your second variable is:", second)
print("your third variable is:", third)
