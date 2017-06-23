import os
import paramiko
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




# @tools.route('vod_show')
# def vod_show():
