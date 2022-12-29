#  split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
# str.split(str="", num=string.count(str)).
# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# join 将前面的东西加到字符串中间来返回行的字符串 加到里面的东西.join(要链接的序列) 是一种list变成字符串的方法
ten_things = "Apples Oranges Crows Telephone Light Suger"

print("Wait there are not 10 thing in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]


while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

    print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))  # what? cool!
print('#'.join(stuff[3:5]))  # super stellar!
# 习题未完成