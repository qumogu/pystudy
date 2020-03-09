#一个死循环任务
import threading 

def deadloop():
    while True:
        pass
    
def main():
    
    t1 = threading.Thread(target=deadloop)
    t1.start()

    while True:
        pass


if __name__ == "__main__":
    main()
