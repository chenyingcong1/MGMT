import os
import paramiko
import sqlite3
from datetime import datetime
import socket
import nmap
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
    conn = sqlite3.connect(DATABASE_URL)
    c = conn.cursor()
    sql="select rowid,ip,team from ShutdownIP"
    sql1="select DISTINCT team from ShutdownIP"
    lis = c.execute(sql).fetchall()
    team = c.execute(sql1).fetchall()
    conn.commit()
    return render_template('power.html',lis=lis,team=team)

@tools.route('/monitor_add/',methods=['GET','POST'])
def monitor_add():
    if request.method == 'POST':
        ip = request.form.get('ip')
        team = request.form.get('team')
    conn = sqlite3.connect(DATABASE_URL)
    c = conn.cursor()
    sql1 = "insert into ShutdownIP (ip,team) values (?,?)"
    c.execute(sql1, (ip, team))
    conn.commit()
    return redirect(url_for('tools.monitor'))


@tools.route('/shutdown/',methods=['GET','POST'])
def shutdown():
    if request.args.get('address'):
        remoteIP = request.args.get('address')
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((remoteIP, 4000))
            sock.send('register'.encode())
            recv = sock.recv(1024).decode()
            if 'success' in recv:
                while 1:
                    ent = 'shutdown'
                    sock.send(ent.encode())
                    res = sock.recv(1024).decode()
                    return redirect(url_for('tools.monitor'))
            sock.close()
        except Exception as e:
            return str(e)



@tools.route('/monitor/time/')
def content():
    return str(datetime.now())

@tools.route('/state/',methods=['GET','POST'])
def state():
    if request.method == 'POST':
        ip = request.form.get('ip')
        return "<i class='fa fa-check-square fa-lg'></i>"

@tools.route('/password/',methods=['GET','POST'])
def password():
    if request.method == 'POST':
        inputpassword = request.form.get('password')
        if inputpassword == 'cutv.com':
            return redirect(url_for('tools.monitor'))
        else:
            return render_template('password.html')
    elif request.method == 'GET':
        return render_template('password.html')
        # nm = nmap.PortScanner()
        # if nm.scan('{}'.format(ip), '22')['nmap']['scanstats']['downhosts'] == 1:
        #     return 'down'
        # elif nm.scan('{}'.format(ip), '22')['nmap']['scanstats']['downhosts'] == 0:
        #     return 'up'
        # return ip

        # nm = nmap.PortScanner()
        # if nm.scan('192.168.1.41', '22')['nmap']['scanstats']['downhosts'] == 1:
        #     return 'down'
        # elif nm.scan('192.168.1.41', '22')['nmap']['scanstats']['downhosts'] == 0:
        #     return 'up'

# @tools.route('/monitor/CPU/',methods = ['GET','POST'])
# def get_cpu():
#     if request.method == 'GET':

