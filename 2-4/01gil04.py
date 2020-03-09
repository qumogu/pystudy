#一个死循环任务
import threading 

#导入C语言的拓展模块
from ctypes import *

   
def main():
    
    
    #加载C语言编译后的动态库
    lib = cdll.LoadLibrary("./libdeadloop.so")    

    #创建一个子线程，让其执行c语言的的函数，此函数是一个死循环
    t1 = threading.Thread(target=lib.DeadLoop)
    t1.start()

    while True:
        pass


if __name__ == "__main__":
    main()
