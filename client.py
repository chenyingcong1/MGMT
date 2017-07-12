import socket, time

def Client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('172.16.7.81',4000))
    while 1:
        print('enter something:')
        ent =input()
        if ent == '':
            break
        sock.send(str.encode(ent))
        time.sleep(1)
        data =sock.recv(1024)
        print('echo=>',data)
    sock.close()
if __name__ == '__main__':
    Client()

# import socket
#
# obj = socket.socket()
# obj.connect_ex(("127.0.0.1",8080))
#
# ret = str(obj.recv(1024),encoding="utf-8")
# print(ret)