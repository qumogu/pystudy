#一个死循环任务
#多一个死循环进程
import multiprocessing 

def deadloop():
    while True:
        pass
    
def main():
    
    p1 = multiprocessing.Process(target=deadloop)
    p1.start()

    p2 = multiprocessing.Process(target=deadloop)
    p2.start()
    
    while True:
        pass


if __name__ == "__main__":
    main()
