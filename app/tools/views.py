import os
import paramiko
import sqlite3
from datetime import datetime
import socket
import time
from stat import S_ISDIR

from flask import request, render_template, redirect, url_for, send_from_directory,make_response
from flask import Blueprint
from app.tools import tools



DATABASE_URL = os.path.realpath('./db/contract.db')


@tools.route('/find_vod/')
def find_vod():
    return render_template('vod_find.html')

@tools.route('/vod_post/',methods=['POST'])
def vod_post():
    if request.method == 'POST':
        url = str(request.form.get('vod_url'))
        head = ['http://videofile1.cutv.com/originfileg','http://videofile2.cutv.com/vg','http://videoimage1.cutv.com/originfileg']
        for i in head:
            if i in url:
                real_url = url.replace(i,'/data/vod7')
                break
            else:pass
    filelist = []
    filetag = real_url.split('/')[-1].split('_')[0]
    path = '/'.join(real_url.split('/')[:-1])
    client = paramiko.Transport(('10.20.100.86',50289))
    client.connect(username='root',password='1vu~Teh*(*eELuK23yd(YTG')
    sftp = paramiko.SFTPClient.from_transport(client)
    files = sftp.listdir(path)
    for f in files:
        if filetag in f:
            filelist.append(path+'/'+f)
    if filelist:
        for i in filelist:
            sftp.remove(i)
        result = '文件已删除'
    else:result =  '文件不存在'
    return render_template('vod_show.html',filelist = filelist,result = result)




@tools.route('/show_ip/',methods=['GET','POST'])
def show_ip():
    if request.args.get('name'):
        name = request.args.get('name')
        mask = request.args.get('mask')
        conn = sqlite3.connect(DATABASE_URL)
        c = conn.cursor()
        sql = "select * from {}".format(name)

        tablelis = c.execute(sql)
        conn.commit()
        return render_template('iptable.html', name=name, mask=mask, tablelis=tablelis)
    else:
        conn = sqlite3.connect(DATABASE_URL)
        c = conn.cursor()
        sql = "select * from IPsubnet"
        lis = c.execute(sql)
        conn.commit()
        return render_template('iptable.html', lis=lis)




@tools.route('/ip_post/',methods=['POST'])
def ip_post():
    if request.method == 'POST':
        netname = request.form.get('netname')
        netmask = str(request.form.get('netmask'))


    conn = sqlite3.connect(DATABASE_URL)
    c = conn.cursor()
    sql1 = "insert into IPsubnet (name,netmask) values (?,?)"
    c.execute(sql1,(netname,netmask))
    conn.commit()
    sql2 = """CREATE TABLE {}(IP TEXT);""".format(netname)
    c.execute(sql2)
    conn.commit()


    cut = netmask.split('/')[0].split('.')

    for i in range(1,(2**(32-int(netmask.split('/')[1]))-1)):
        ip = str(cut[0]+'.'+cut[1]+'.'+cut[2]+'.'+str(int(cut[3])+i))
        sql3 = """insert into {} (IP) values (?)""".format(netname)
        c.execute(sql3,(ip,))
        conn.commit()
    conn.close()


    return redirect(url_for('tools.show_ip'))


@tools.route('/monitor/')
def monitor():
    locakIP = socket.gethostbyname(socket.gethostname())
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((locakIP, 4000))
    sock.listen(10)
    iptable = []
    while 1:
        try:
            connection, address = sock.accept()
            while 1:
                data = connection.recv(1024).decode()
                if not data:
                    break
                elif data == 'register':
                    iptable.append(address[0])
                    connection.send("register success".encode())
                else:
                    if data:
                        connection.send('ok'.encode())
        except ConnectionResetError as e:
            print(e,)
            time.sleep(4)
    pid = [1,2]
    return render_template('poweroff.html',ip=iptable,pid =pid)

@tools.route('/monitor/time/')
def content():
    return str(datetime.now())

# @tools.route('/monitor/CPU/',methods = ['GET','POST'])
# def get_cpu():
#     if request.method == 'GET':

