
import socket

def main():

    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    listen_addr = ("",3344)

    udp_socket.bind(listen_addr)

    recv_data = udp_socket.recvfrom(1024)

    print("%s : %s" %(str(recv_data[1]),recv_data[0]))

    udp_socket.sendto(b'i had got your msg',recv_data[1])

    udp_socket.close()


if __name__ == "__main__":
    main()
