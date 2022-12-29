# 比起之前用if语句编写的小游戏class好像更加的方便，之前的def直接变成了class而且相同的class可以继承非常方便
# randint（起点，终点）传回一个起点到终点的随机数
# dedent删除字符串中的前导空格就是为了美观好像没用    print（dedent（内容））这样输出可以保证代码格式美观而且输美观


# 调用库
from sys import exit              # 退出库
from random import randint        # 随机数库
from textwrap import dedent       # 去头空格的美观库


class Scene:

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)                  # 退出并返回1


class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a user.",
        "I have a small puppy that's better at this.",
        "You're worse than yor Dad's jokes"
    ]                   # 建立了一个列表

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)]) # 调用Death里面的列表quips传入随机数(0到quips长度-1)作为参数并输出-------时间一个死法
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Goons of Planet Percale #25 have invaded your ship and 
            destroyed your entire crew. You are the last surviving 
            member and your last mission is to get the neutron destruct 
            bomb from the Weapons Armory, put it in the bridge, and 
            blow the ship up after getting into an escape pod. 
            You're running down the central corridor to the Weapon
            Armory when a Goon jumps out, red scaly skin, dark grimy 
            teeth, and evil clown costume flowing around his hate 
            filled body. He's blocking the door to the Armory and 
            about to pull a weapon to blast you.
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire
                it at the Goon. His clown costume is flowing and
                moving around his body, which throws off your aim.
                Your laser hits his costume but misses him entirely.
                This completely ruins his brand new costume his mother
                bought him, which makes him fly into an insane rage
                and blast you repeatedly in the face until you are
                dead. Then he eats you.
                """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                    Like a world class boxer you dodge, weave, slip and
                    slide right as the Goon's blaster cranks a laser
                    past your head. In the middle of your artful dodge
                    your foot slips and you bang your head on the metal
                    wall and pass out. You wake up shortly after only to
                    die as the Goon stomps on your head and eats you.
                    """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                        Lucky for you they made you learn Goon insults                             
                        the academy. You tell the one Goon joke you know:
                        Lobe Figure vf fb sng, jira fur fig nebulae gur uber,
                        fur fog nebulae gur uber. The Goon stops, tri      
                        not to laugh, then busts out laughing and can't move.
                        While he's laughing you run up and shoot him square
                        the head putting him down, then jump throughWeapon Armory door.
                        """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):         # 激光武器库

    def enter(self):
        print(dedent("""
                    You do a dive roll into the Weapon Armory, crouch and scan
                    the room for more Goons that might be hiding. It's dead
                    quiet, too quiet. You stand up and run to the far side of
                    the room and find the neutron bomb in its container.
                    There's a keypad lock on the box and you need the code to
                    get the bomb out. If you get the code wrong 10 times then
                    the lock closes forever and you can't get the bomb.  The
                    code is 3 digits.
                    """))

        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BUZZED!")
            guesses += 1
            guess = input("[keypad]> ")

            if guess == code:
                print(dedent("""
                        The container clicks open and the seal breaks, letting
                        gas out. You grab the neutron bomb and run as fast as
                        you can to the bridge where you must place it in the
                        right spot.
                        """))
                return 'the_bridge'
            else:
                print(dedent("""
                        The lock buzzes one last time and then you hear a
                        sickening melting sound as the mechanism is fused
                        together. You decide to sit there, and finally the
                        Goths blow up the ship from their ship and you die.
                        """))
                return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
                    You burst onto the Bridge with the neutron destruct bomb
                    under your arm and surprise 5 Goons who are trying to
                    take control of the ship. Each of them has an even uglier
                    clown costume than the last. They haven't pulled their
                    weapons out yet, as they see the active bomb under your
                    arm and don't want to set it off.
                    """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                        In a panic you throw the bomb at the group of Goons
                        and make a leap for the door. Right as you drop it a
                        Goon shoots you right in the back killing you.  As
                        you die you see another Goon frantically try to
                        disarm the bomb. You die knowing they will probably
                        blow up when it goes off.
                        """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                        You point your blaster at the bomb under your arm and
                        the Goons put their hands up and start to sweat.
                        You inch backward to the door, open it, and then
                        carefully place the bomb on the floor, pointing your
                        blaster at it. You then jump back through the door,
                        punch the close button and blast the lock so the
                        Goons can't get out. Now that the bomb is placed
                        you run to the escape pod to get off this tin can.
                        """))

            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return 'the_bridge'


class EscapePod(Scene):
    def enter(self):
        print(dedent("""
                    You rush through the ship desperately trying to make it to
                    the escape pod before the whole ship explodes. It seems
                    like hardly any Goons are on the ship, so your run is
                    clear of interference. You get to the chamber with the
                    escape pods, and now need to pick one to take.  Some of
                    them could be damaged but you don't have time to look.
                    There's 5 pods, which one do you take?
                    """))

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                        You jump into pod {guess} and hit the eject button.
                        The pod escapes out into the void of space, then
                        implodes as the hull ruptures, crushing your body into
                        jam jelly.
                        """))

            return 'death'
        else:
            print(dedent(f"""
                        You jump into pod {guess} and hit the eject button.
                        The pod easily slides out into space heading to the
                        planet below. As it flies to the planet, you look
                        back and see your ship implode then explode like a
                        bright star, taking out the Goon ship at the same
                        time. You won!
                        """))

            return 'finished'


class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Engine:
    # 在类里面存了个scene_map
    def __init__(self, scene_map):
        self.scene_map = scene_map

    # 1.开始游戏调用play    -----opening_scene /256
    def play(self):
        current_scene = self.scene_map.opening_scene()   # 当前场景
        last_scene = self.scene_map.next_scene('finished') # 最后的场景
        # 没用结束时
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()    # 这个时候已经开始游戏了，enter为当前场景覆盖的函数，并把当前的enter返回的新地图带入到next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)   # 利用next_scene_name调用函数 next_scene

        # be sure to print out the last scene

        current_scene.enter()


class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    # 开始游戏，初始场景为创建Map时带入的参数，一般为central_corridor(中央走廊)
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')     # 由Map类 生成a_map对象带入参数地图中间
a_game = Engine(a_map)              # 由Engine类继承a_map生成对象a_game
a_game.play()                       # 调用a_game里的play函数

