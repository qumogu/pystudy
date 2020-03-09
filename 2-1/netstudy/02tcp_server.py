import socket

def main():
    
    #1.创建服务端套接字
    lis_ser_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2.绑定监听端口
    lis_ser_socket.bind(("",4546))
    
    #3.套接字变被动连接
    lis_ser_socket.listen(128)
    print("------1--------")

    while True:
        print("等待下一个客户的接入:")
        #4.等待客户连接

        new_ser_socket,client_addr = lis_ser_socket.accept()
        print(client_addr)
        
        while True:
            #5.接收客户端信息并回应
            recv_data = new_ser_socket.recv(1024)
            if recv_data:
                print(recv_data)
                new_ser_socket.send("msg is over.-------ok------".encode("utf-8"))
            else:
                break

        new_ser_socket.close()

    lis_ser_socket.close()
    print("tcp server close")

if __name__ == "__main__":
    main()
