import multiprocessing
import time

def test3():


def test1():
    for i in range(10):
        print("-----进程1------")
        time.sleep(1)

def test2():
    for i in range(20):
        print("-----进程2------")
        time.sleep(1)

def main():

    p1 = multiprocessing.Process(target = test1)
    p2 = multiprocessing.Process(target = test2)

    p1.start()
    p2.start()

    for i in range(30):
        print("-----主进程------")
        time.sleep(1)




if __name__ == "__main__":
    main()
