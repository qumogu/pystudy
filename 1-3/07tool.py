

class Tool(object):
    """工具类"""

    #定义类属性
    toolnum = 0


    def __init__(self,name):

        self.name = name
        Tool.toolnum += 1

    def __del__(self):
        
        print("%s已经删除" % self.name)
        Tool.toolnum -= 1


t1 = Tool("斧头")
t2 = Tool("锤子")
print(Tool.toolnum)
t3 = Tool("尺子")
print(Tool.toolnum)
del t2

print(Tool.toolnum)





