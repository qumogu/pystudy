# *—* encoding:UTF-8 *—*

import os
import time

def main():

    filename = input("请输入要文件或目录名：")
    # newfilename =  input("请输入新的文件名：")
    # os.rename(filename, newfilename)
    
    print(os.getcwd())
    os.mkdir(filename)
    time.sleep(1)
    os.rmdir(filename)
    time.sleep(1)
    files = os.listdir("10import")
    
    for f in files:
        
        path = "10import/" + f
        # print(path)
        if os.path.isdir(path):
            print("%s 是目录" % f)
        else:
            print("%s 是文件" % f)



if __name__ == "__main__":
    main()