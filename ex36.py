from sys import exit


# 得分函数


def fraction(gold):
    fraction_all = 0
    while gold > 0:
        fraction_all += 500
        gold -= 1
    return fraction_all


# 游戏结束了函数
def win_game(fraction_all):
    print("恭喜你获得胜利.")
    print("你的得分是", fraction_all)


# 死亡函数
def dead(reason):
    print("good job"
          "Game over")
    print("游戏结束了你死于", reason)


# 提示函数
def tips(tip):
    print("在下面的关卡中请好好利用", tip)
    print("祝你通关顺利.")


# 向右第一口，道具房间
def props_room_1(gold_):
    print("""你来到了一个神奇的房间
    你面前有俩种物品
    1.钥匙
    2.魔法棒
    选择带走哪一个.""")
    props = int(input("你要带走什么: "))
    if props == 1:
        tips("钥匙")
    elif props == 2:
        tips("魔法棒")
    else:
        print("请按照游戏规则来进行游戏.")
        exit(0)

    print("""你现在面临分叉路口
    可选择继续:
    1.向前
    2.向右
    前面有奇怪的声音传来还是不要走比较好.
    """)
    intersection_1 = int(input("旅行者你要前往何方."))
    #   一路口前往三路口（完成）
    if intersection_1 == 2:
        print("""你现在面临分叉路口
        可选择继续
        1.向前
        2.向右
        前方的墙壁好像需要魔法才可以打开
        右边的门好像需要钥匙才可以打开""")
        intersection_3 = int(input("> 选择你的道路."))
        # 三路口前往五路口（完成）
        if intersection_3 == 1 and props == 2:
            print("""恭喜你使用魔法打开了大门.
            你发现了黄金并带走了它们. 
            现在再次面临分岔路口.
            前面散发着金色的光芒你要去吗.
            可选择继续:
            \t1.向前
            \t2.向右""")
            gold_ += 1
            intersection_5 = int(input("你要前往何方."))
            # 五路口结局口
            if intersection_5 == 1:
                dead("贪婪")
            elif intersection_5 == 2:
                win_game(fraction(gold_))
        #  三路口前往四路口（完成）
        if intersection_3 == 2 and props == 1:
            print("你发现了黄金."
                  "并带走了它们.")
            gold_ += 1
            print("""你面前是分岔路口：
            前面可直行.
            右边需要爬上去，没有工具无法攀爬.
            左边好像很安全.""")
            print("""选择你的方向:
            1.强行攀爬
            2.向前探索
            3.安稳向左""")
            # 四路口结局
            intersection_4 = int(input("选择你的方向"))
            if intersection_4 == 1:
                print("你真的超勇的.")
                dead("没有道具，跌落死亡")
            if intersection_4 == 3:
                print("果然平平无奇."
                      "你逃离了这里."
                      "什么都没有发生.")
            if intersection_4 == 2:
                print("哎哟不错哟."
                      "你发现了水晶")
                gold_ += 1
            else:
                exit(0)

#  三路口没选对结局 （完成）

        if intersection_3 == 2 and props == 2:
            print("明明告诉你要带钥匙的呀")
            dead("饿死了.")
        if intersection_3 == 1 and props == 1:
            print("没看见提示吗.")
            dead("门放出来的魔法.")
# 一路口向前（完成）
    if intersection_1 == 1:
        print("好奇心会害死猫.")
        dead("怪物的攻击.")


def props_room_2(gold_):
    print("""现在你面前有俩种物品：
    3.水晶
    4.弓箭
    你仅仅可以带走一个""")
    props = int(input("你的选择是"))
    if props == 3:
        gold_ += 1

    else:
        tips("弓箭")

    print("""前面好像很可怕
    左边好像很安全但是好黑
    1.我不听我不听我要去前面
    2.好吧那就走左边""")
    intersection_2 = int(input("选择你的方向"))
    if intersection_2 == 1 and props == 3:
        print("你打败了这里的怪物但是没有受伤了，刚刚好前面就是出口你逃走了.")
        win_game(fraction(gold_))
    if intersection_2 == 1 and not props == 3:
        print("前面有怪物但是你没有武器，你被击杀了")
        dead("贪婪，还胆大.")
    if intersection_2 == 2:
        print("""你面前出现了分岔路口
        1.右边发出了光芒去右边
        2.继续在黑暗中前进""")
        intersection_4 = int(input("选择你的道路."))
        if intersection_4 == 1:
            print("太棒了你发现了水晶")
            gold_ += 1
        if intersection_4 == 2:
            print("这里还是什么都没有")
            win_game(fraction(gold_))


def main():
    print("""你在下面的游戏中要选择前面的数字
    加油活下来
    选择你的方向
    1.向右
    2.向左""")
    gold_ = 0
    first = int(input("> "))
    if first == 1:
        props_room_2(gold_)
    if first == 2:
        props_room_1(gold_)
    if not first == 1 and not first == 2:
        exit(0)


main()