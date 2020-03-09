import time

def work1():
    for i in range(1,10):
        print("---第%d次执行work1---" % i)
        yield
        time.sleep(0.2)
    return "work1,111111!"


def work2():
    for i in range(1,10):
        print("---第%d次执行work2---" % i)
        yield
        time.sleep(0.1)
    return "work2,game over!"

def work3():
    for i in range(1,5):
        print("---第%d次执行work3---" % i)
        yield
        time.sleep(0.5)
    return "work3,33333!"


def main():
    w1 = work1()
    w2 = work2()
    w3 = work3()
    
    while True:
        try:
            next(w1)
            next(w2)
            next(w3)
        except StopIteration as e:
            print("线程结束", e.value)
            break
if __name__ == "__main__":
    main()
