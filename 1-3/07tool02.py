

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
print(t1.toolnum)
t3 = Tool("尺子")

# 给实例的类属性赋值，并不会改变类属性的值，而是会给实例新增一个属性
t3.toolnum = 10 
print(Tool.toolnum)
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




