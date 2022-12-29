class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):

    # 重要的组合操作

    def __init__(self):
        self.other = Other()

    def override(self):
        print("CHILD override()")

    def implicit(self):
        # 在这里调用other里面的函数
        self.other.implicit()

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


son = Child()

son.implicit()
son.override()
son.altered()
