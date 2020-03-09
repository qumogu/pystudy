import threading
import time

number = 0

def addnum1(nums):
    global number
    print("-----自增测试1-----")
    for i in range(nums):
        number += 1
    print("自增结束的number的值：%d。" %number)


def addnum2(nums):
    global number
    print("-----自增测试2-----")
    for i in range(nums):
        number += 1
    print("自增结束的number的值：%d。" %number)


def main():
    t1 = threading.Thread(target = addnum1,args = (5000000,))
    t2 = threading.Thread(target = addnum1,args = (5000000,))
    
    t1.start()
    t2.start()

    time.sleep(0.5)

    print(number)

    time.sleep(0.5)
    print(number)

    time.sleep(1)
    print(number)


if __name__ == "__main__":
    main()
