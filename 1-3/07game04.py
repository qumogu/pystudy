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
        print("这是一个中奖游戏，玩法很简单。\n1、开始游戏后输入您的名字；\n2、等待系统给您抽奖，公布分数。\n3、判断您的奖项。\n现在您可以输入姓名开始了。") 
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
            Game.g_score = now_score
            Game.g_name = self.p_name
        time.sleep(1)
            
def get_score(p_name,num):
    g1 = Game(p_name)
    print("欢迎第%d个玩家【%s】加入游戏" % (Game.player_num, p_name))
    
    i = 0
    while i < num:
        g1.open_score()
        i += 1
    print("玩家【%s】已完成次%d抽奖." % (p_name, num))

    

def main():

    Game.show_help()
    time.sleep(1)
    while True:
        p_name = input("请输入玩家的名字：")
        if p_name == "exit":
            break

        t1 = threading.Thread(target=get_score, args=(p_name,5))
        t1.start()
        #get_score(p_name, 2) 


    Game.game_over()
    

if __name__ == "__main__":
    main()
