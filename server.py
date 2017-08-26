import socket, time
def Server():
    locakIP = socket.gethostbyname(socket.gethostname())
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((locakIP,4000))
    sock.listen(10)
    print("server start")
    # sock.settimeout(8)
    while 1:
        try:
            connection, address = sock.accept()
            count =0
            while 1:
                data = connection.recv(1024).decode()
                if not data:
                    break
                elif data == 'register':
                    print('Client:'+address[0]+' connect success')
                    connection.send("register success".encode())
                else:
                    if data:
                        count=count+1
                        connection.send('ok'.encode())
                        print(data+str(count))
            connection.close()
        except ConnectionResetError as e:
            count = count-1
            print(e+str(count))
            time.sleep(4)
if __name__ == '__main__':
    Server()