title = "模块2"

def say_hello():
    print("%s:正在使用中……" % title)

class Cat(object):

    def __init__(self, name):
        self.name = "小猫-" + name
    
    def run_speed(self, speed):
        print("%s：正在以【%d】km/h的速度奔跑……" % (self.name, speed))

    def __str__(self):
        return "我是可爱的%s,快来抱抱我……" % self.name