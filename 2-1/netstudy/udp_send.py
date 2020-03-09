import socket

def main():
    print("hello python")
    upd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    msg = 
    upd.sendto(msg,("192.168.1.101",8080))
    upd.close()
    print("send successfully")


if __name__ == "__main__":
    main()
