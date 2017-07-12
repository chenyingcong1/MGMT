import socket

def Server():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('192.168.108.16',4000))
    sock.listen(10)
    while 1:
        connection, address = sock.accept()
        while 1:
            data = connection.recv(1024)
            if not data:
                break
            print(data, address)
            connection.send(data)
        connection.close()

if __name__ == '__main__':
    Server()

# import socket
#
# sk = socket.socket()
# sk.bind(("127.0.0.1",8080))
# sk.listen(5)
#
# conn,address = sk.accept()
# sk.sendall(bytes("Hello world",encoding="utf-8"))