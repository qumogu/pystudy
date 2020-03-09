import random
import time 

class Game(object):
    """游戏类，记录显示最高分"""
    
    #最高得分记录
    g_score = 0
    g_name = None

    #静态函数，游戏帮助
    @staticmethod
    def show_help():
        print("这是一个中奖游戏，玩法很简单。\n1、开始游戏后输入您的名字；\n2、等待系统给您抽奖，公布分数。\n3、判断您的奖项。\n现在您可以输入姓名开始了。") 
    time.sleep(1)
    print("*" * 50)


    #类函数，显示最高得分
    @classmethod
    def show_score(cls):
        if cls.g_name is None:
            print("游戏还没有人玩过。")
        else:
            print("游戏最高分是由【%s】获得的【%d】" % (cls.g_name,
            cls.g_score))
    

    def __init__(self,name):
        self.p_name = name
        self.p_score = 0

    def open_score(self):
        now_score = random.randint(1,101)

        if now_score > Game.g_score:
            print("恭喜【%s】，超过【%s】【%d】的历史最高分,创造新的记录" %
            (self.p_name, Game.g_name, Game.g_score))
            time.sleep(2)
            Game.g_score = now_score
            Game.g_name = self.p_name
            Game.show_score()
            time.sleep(1)
        else:
            print("恭喜【%s】，获得【%d】分，还未打破记录" % (self.p_name,
            now_score))
            time.sleep(1)
            
def main():

    Game.show_help()
    time.sleep(1)
    p_name = input("请输入玩家的名字：")
    g1 = Game(p_name)
    g1.open_score()
    time.sleep(2)

    g1.open_score()
    time.sleep(2)

    print("最后让我们看看后的得分情况：")
    Game.show_score()
    time.sleep(1)
    print("game over!")


if __name__ == "__main__":
    main()
