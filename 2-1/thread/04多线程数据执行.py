import threading
import time

user_nums = 100

user_list =["jack","lily"]

mutex = threading.Lock()

def test1():
    mutex.acquire()
    global user_nums 
    user_nums += 100
    user_list.append("tom")
    time.sleep(1)
    print_args()
    mutex.release()

def test2():
    mutex.acquire()
    user_nums = 300
    user_list.append("may")
    time.sleep(1)
    print_args()
    mutex.release()

def print_args():
    print(user_nums)
    print(user_list)

def main():
    t1 = threading.Thread(target = test1)
    t2 = threading.Thread(target = test2)
    
    print("-----开始-----")
    print_args()
    t1.start()
    t2.start()
    
    #time.sleep(2)

    print("-----结束前----")

    print_args()
    print("-----结束-----")



if __name__ == "__main__":
    main()
