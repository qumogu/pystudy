"""
相比04更改如下：

1、一次性行输入玩家信息，
2、系统自动完成多线程的玩家抽奖
"""


import random
import time 
import threading

class Game(object):
    """游戏类，记录显示最高分"""
    
    #最高得分记录
    g_score = 0
    g_name = None
    player_num = 0

    #静态函数，游戏帮助
    @staticmethod
    def show_help():
        print("这是一个中奖游戏，玩法很简单。\n1、先逐一输入玩家姓名和抽奖次数；\n2、等待系统给您抽奖，公布分数。\n3、注意玩家姓名输入exit时结束输入。\n现在您可以开始输入玩家信息了。") 
        time.sleep(1)
        print("*" * 50)


    #类函数，显示最高得分
    @classmethod
    def show_score(cls):
        if cls.g_name is None:
            print("游戏还没有人玩过。")
        else:
            print("本次游戏一共有%d人参与，游戏最高分是由【%s】获得的【%d】" %
            (cls.player_num, cls.g_name,cls.g_score))
   
    
    @classmethod
    def game_over(cls):
        
        print("-" * 40)
        print("")
        print("让我们看看最后的得分情况：")
        cls.show_score()
        time.sleep(1)
        print("game over!")


    def __init__(self,name):
        self.p_name = name
        self.p_score = 0
        Game.player_num += 1

    def open_score(self):
        now_score = random.randint(1,101)

        if now_score > Game.g_score:
            if Game.g_name is None:             
                print("恭喜【%s】以【%d】的高分,抢得第一次游戏最高记录" %
                (self.p_name, now_score))
            else:
                print("恭喜【%s】以【%d】的高分，超过【%s】【%d】的历史最高分,创造新的记录" %
                (self.p_name, now_score, Game.g_name, Game.g_score))
            Game.g_score = now_score
            Game.g_name = self.p_name
            #Game.show_score()
            #time.sleep(1)
        else:
            print("恭喜【%s】，获得【%d】分，还未打破记录" % (self.p_name,
            now_score))
        time.sleep(1)
            
def get_score(p_name,num):
    g1 = Game(p_name)
    print("欢迎第%d个玩家【%s】加入游戏" % (Game.player_num, p_name))
    time.sleep(random.random())

    i = 0
    while i < num:
        g1.open_score()
        i += 1
    print("玩家【%s】已完成次%d抽奖." % (p_name, num))


def get_games():

    t_games = list()
    while True:
        p_name = input("请输入玩家的名字：")
        if p_name == "exit":
            print("玩家入场完毕，抽奖开始！")
            time.sleep(1)
            break
        try:
            num = int(input("请输入玩家抽奖次数，最多9次:"))
            if num < 1 or num > 9:
                print("您输入数字不在1-9之间，系统自动改为5次！")
                num = 5
        except:
            print("您输入的非数字，系统自动改为5次！")
            num = 5
        t = threading.Thread(target=get_score, args=(p_name, num))
        t_games.append(t)
    return t_games

    
def main():

    #显示游戏帮助
    Game.show_help()
    time.sleep(1)
    
    #获取玩家信息
    t_games = get_games()

    #开启所有玩家抽奖
    for t_game in t_games:
        t_game.start()
    
    #等待所有抽奖结束
    for t_game in t_games:
        t_game.join()

    #显示游戏结束信息
    Game.game_over()
    

if __name__ == "__main__":
    main()
