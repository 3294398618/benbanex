# import math
# # 由sin的值来得到角度 单位为弧度。1弧度等于57.3度
# print(math.asin(0.5))

# 局部变量变成全局变量，内可以该外面
Money = 2000


def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1


print(Money)
AddMoney()
print(Money)