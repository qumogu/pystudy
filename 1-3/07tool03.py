import time

class Tool(object):
    """工具类"""

    #定义类属性
    toolnum = 0

    @classmethod
    def show_toolnum(cls):
        
        print("当前类现在有%d个实例。" % cls.toolnum)


    @staticmethod
    def show_help():
        
        print("Welcome to toolboxes,Please chose your tools")


    def __init__(self,name):

        self.name = name
        Tool.toolnum += 1

    def __del__(self):
        
        print("%s已经删除" % self.name)
        Tool.toolnum -= 1

    def add_num(self, num):
        
        Tool.toolnum += num
        print("类属性加%d" % num)


    def get_tool(self):

        print("恭喜您获得【%s】" % self.name)
        time.sleep(1)

def main():

    Tool.show_help()
    time.sleep(1)

    t1 = Tool("斧头")
    t1.get_tool()
    t2 = Tool("锤子")
    t2.get_tool()
    print(Tool.toolnum)
    print(t1.toolnum)
    t3 = Tool("尺子")
    t3.get_tool()

    # 给实例的类属性赋值，并不会改变类属性的值，而是会给实例新增一个属性
    #t3.add_num(10)
    #print(Tool.toolnum)
    Tool.show_toolnum()

    del t2
    #下面调用的是实例属性toolnum，而非类属性
    print(t3.toolnum)
    #t1没有实例属性，所以向上查找类属性，显示的是类属性。
    print(t1.toolnum)
    print(Tool.toolnum)


    Tool.toolnum = 10
    t4 = Tool("刀")
    print(t1.toolnum)
    print(Tool.toolnum)
    #类属性的值，可以通过在外部直接赋值改变，也可以在类的方法里面改变，而无法实例去改变。


if __name__ == "__main__":
    main()





