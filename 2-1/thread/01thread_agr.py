import threading
import time


def login(name,pwd):
    if pwd == "python":
        for i in range(5):
            print("-----%s：您好，系统第%d次挣钱-----" %(name,i+1))
            time.sleep(1)
    else:
        print("%s:您好，密码不对，无法为您挣钱." %name)
        time.sleep(2)
        reg_user(name)

def reg_user(name):

    print("%s:您好，系统正在为您注册数据。" %name)
    time.sleep(2)
    print("%s:您好，已经注册好，请记住密码是：python" %name)


def main():
    t1 = threading.Thread(target = login,args = ("Jack","python"));
    t2 = threading.Thread(target = login,args = ("Lily","python123"));
    t3 = threading.Thread(target = login,args = ("Tom","python"));

    t1.start()
    t2.start()
    t3.start()



if __name__ == "__main__":
    main()
