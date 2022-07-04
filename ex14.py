# input的提示语可以用变量表示/方便统一修改
from sys import argv

script, user_name = argv
prompt = '>'

print(f"hi {user_name}, i'm the {script} script.")
print("i'd like to ask you a few questions.")
print(f"do you like me {user_name}?")
likes = input(prompt)    # 在要求输入时会在前面显示prompt（>）

print(f"where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have ?")
computer = input(prompt)

print(f"""
alright,so you said {likes} about liking me.
you live in {lives}.not suer where that is.
and you have a {computer} computer. nice.""")