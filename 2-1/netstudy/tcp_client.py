
import socket

def main():
    print("ok")
    #1.创建TCP的套节字
    tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_client.connect(("192.168.1.112",8080))
    send_data = input("请输入要发送的数据:")

    tcp_client.send(send_data.encode("UTF-8"))

    tcp_client.close()
    print("客户端关闭")


if __name__ == "__main__":

    main()
