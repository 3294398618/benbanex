class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()
# implicit为son在dad那里直接继承的函数操作，会调用dad里面的同名函数
dad.implicit()
son.implicit()
# override在son与dad里面都有定义，子类里面的定义会在子类里完成覆盖（父类的仍然保留但需要用特殊手段调用），在son里调用override会直接调用自己的不会从父类里面继承
dad.override()
son.override()
# 和前面无差别
# super（子类名，self）.函数名          可在被覆盖的情况下调用在子类里面调用父类函数
dad.altered()
son.altered()
