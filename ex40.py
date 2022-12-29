# 跨项目调用函数需要     项目.函数（）
# mystuff['apple']                       利用字典直接调用
# mystuff.apple()                        调用apple函数
# print（mystuff.tangerine）             调用apple里的值直接输出

# 创建一个类
class Mystuff(object):

    def __init__(self):
        self.tangerine = "and now a thousand years between"

    @staticmethod
    def apple():
        print("i am classy apples!")


# dict style
Mystuff['apples']

# module style
Mystuff.apples()
print(Mystuff.tangerine)

# class style
thing = Mystuff()
thing.apples()
print(thing.tangerine)
