import socket
import threading


def rece_data(udp_socket):
    """接收数据并显示"""
    # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_data(udp_socket, dest_ip, dest_port):
    """发送数据"""
    # 发送数据
    while True:
        send_data = input("输入发送内容:")
        udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))


def main():
    """完成udp聊天室整体控制"""
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定本地信息
    udp_socket.bind(("127.0.0.1", 8000))

    # 3.获取对方IP
    dest_ip = input("请输入对方IP：")
    dest_port = int(input("请输入对方PORT："))

    # 4.创建两个线程
    t_recv = threading.Thread(target=rece_data, args=(udp_socket,))
    t_send = threading.Thread(target=udp_socket, args=(udp_socket, dest_ip, dest_port))
    t_recv.start()
    t_send.start()


if __name__ == '__main__':
    main()
