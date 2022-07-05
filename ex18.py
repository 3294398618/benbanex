# def前面要有俩行空白
# this one like your scripts with argv
def print_tow(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# ok, that *args is actually pointless, we can just do this
def print_tow_gian(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one arguments
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one take no arguments
def print_none():
    print("I got nothin'.")


print_tow("zed", "shaw")
print_tow_gian("zed", "shaw")
print_one("first")
print_none()