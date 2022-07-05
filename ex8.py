# 调用函数formatter
formatter = "{} {} {} {}" # 这里有几个空格就要在下面提供几个变量

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "try your",
    "own text here",
    "maybe a poem",
    "or a song abuot fear"
))