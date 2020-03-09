#from multiprocessing import Pool
import multiprocessing
import time
import os

def po_fun(q,num):
    pid = os.getpid()
    num += 1
    for i in range(1,4):
        print("当下是第%d个任务，进程%d正在执行%d次." % (num,pid,i))
        time.sleep(1)
    q.put((num,pid))
    print("----第%d个任务,执行完成----" % num)

#2.创建消息队列
#q = multiprocessing.Queue(50)
#q = "test"

def main():
    #1.创建进程池
    po = multiprocessing.Pool(3)  #进程池开3个进程

    #2.创建消息队列
    q = multiprocessing.Manager().Queue(50)

    #3.创建进程函数
    print("创建进程函数")

    #4.开启进程池
    for i in range(5):
        print(i)
        po.apply_async(po_fun,args=(q,i))

    #5.主进程监控信息
    time.sleep(1)
    print(str(q.get()))
    po.close()
    po.join()
    print("主进程完成")
if __name__ == "__main__":
    main()
