import time
import multiprocessing

def q_put(q):
    """进程向队列放入数据"""
    put_data = ["11","22","33","44"]

    for i in put_data:
        q.put(i)
        print("队列插入数据%s" % str(i))
        time.sleep(1)
    print("插入结束")

def q_get(q):
    """进程从队列获取数据"""
    get_data = list()

#    while True:
#        if q.empty():
#            break
    data = q.get()
    get_data.append(data)
    print("从队列获取数据%s" % str(data))
#    time.sleep(1.1)
    if q.empty():
        print("数据已取完")

q = multiprocessing.Queue(5)

def main():
    p1 = multiprocessing.Process(target = q_put , args = (q,))
    p2 = multiprocessing.Process(target = q_get , args = (q,))

    print("进程使用队列开始")
    time.sleep(1)

    p1.start()
    p2.start()

    print("主进程结束")

 

if __name__ == "__main__":
    main()


