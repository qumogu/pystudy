title = "Dog Model"

def say_hello():
    print("%s:正在使用中……" % title)

class Dog(object):

    def __init__(self, name):
        self.name = "小狗-" +  name
    
    def eat_food(self, food):
        print("%s：正在吃【%s】" % (self.name, food))

    def __str__(self):
        return "我是可爱的%s,快来和我玩……" % self.name