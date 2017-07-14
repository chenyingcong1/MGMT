import socket, time, psutil, os

def Client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(30)
    while True:
        try:
            sock.connect(('192.168.108.16',4000))
            break
        except:
            print("retry 4 sec later...")
            time.sleep(4)

    sock.send('register'.encode())
    recv = sock.recv(1024).decode()
    if 'success' in recv:
        while 1:
            # print('enter something:')
            # ent =input()
            # if ent == '':
            #     break
            # sock.send(ent.encode())

            #
            # data =sock.recv(1024).decode()
            #
            # print('echo=>',data)
            ent = str(psutil.virtual_memory().percent) +'%'
            sock.send(ent.encode())
            res = sock.recv(1024).decode()
            print(res)
            time.sleep(5)
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