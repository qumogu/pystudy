import time

def main():

    #print(__doc__)

    file = open("readme", "r", encoding="UTF-8")

    file_writer = open("readme-t", "w", encoding="UTF-8")
    
    while True:

        text = file.readline()
        if not text:
            break

        print(text)
        file_writer.write(text)
        time.sleep(1)

    str ="\n" + input("请输入您增加的内容：")
    file_writer.write(str)

    file.close()
    file_writer.close()

if __name__ == "__main__":
    main()