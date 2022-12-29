# Animal is-a object (yes,sort of confusing) look at the extra  credit
class Animal(object):
    pass


# ??创建一个类dog，他是animal的一种
class Dog(Animal):

    def __init__(self, name):
        # ?? 将self里面的参数name赋值为name
        self.name = name


# ?? 定义一个类cat，它属于类animal
class Cat(Animal):

    def __init__(self, name):
        # ?? self里面的参数name赋值为name
        self.name = name


# ?? 定义一个类person，里面有个--init--，他接收self和name为参数
class Person(object):

    def __init__(self, name):
        # ?? 将name的参数赋值name
        self.name = name

        # person has-a pet of some kind
        self.pet = None


class Employee(Person):

    def __init__(self, name, salary):
        # ?? HMM WHAT IS this strange magic?
        super(Employee, self).__init__(name)
        # ??
        self.salary = salary


# ??
class Fish(object):
    pass


# ??
class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# ??
satan = Cat("Satan")

# ??
mary = Person("Mary")

# ??
mary.pet = satan

# ??
frank = Employee("Frank", 120000)

# ??
frank.pet = rover

# ??
flipper = Fish

# ??
crouse = Salmon()

# ??
harry = Halibut()