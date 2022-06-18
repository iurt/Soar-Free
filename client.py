import socket, threading
print("copyright © Zhangmingchen|IURT|Xtian TEAM")
print("欢迎使用Soarfree客户端！")
ip = input("请输入您要连接的服务器的IP:")
port = input("请输入您要连接的服务器的端口:")
port = int(port)
nickname = input("请输入您的昵称: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #socket initialization
client.connect((ip,port))#connecting client to server
print("链接成功！请按Enter继续！")
def receive():
    while True:                                                 #making valid connection
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:                                                 #case on wrong ip/port details
            print("sorry,服务器/客户端可能出了些错误!")
            client.close()
            break
def write():
    while True:                                                 #message layout
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))
receive_thread = threading.Thread(target=receive)               #receiving multiple messages
receive_thread.start()
write_thread = threading.Thread(target=write)                   #sending messages 
write_thread.start()
