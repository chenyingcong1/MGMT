import os
import sqlite3
from datetime import datetime, date

from flask import request, render_template, redirect, url_for, send_from_directory,make_response
from flask import Blueprint
from app.contract import contract

# contract = Blueprint('contract', __name__)


DATABASE_URL = os.path.realpath('./db/contract.db')


# 建立连接
# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE_URL)
#     return db
# # 关闭连接
# @contract.teardown_appcontext
# def close_connection(exeption):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

@contract.route('/creat/')
def contract_creat():
    return render_template('creat-contract.html')

@contract.route('/post_creat/',methods=['POST'])
def post_creat():
    if request.method == 'POST':
        contractname = request.form.get('contractname')
        starttime = request.form.get('starttime')
        endtime = request.form.get('endtime')
        price = request.form.get('price')
        stamp = datetime.now()
        processmax = (datetime.strptime(endtime, '%Y-%m-%d')-datetime.strptime(starttime, '%Y-%m-%d')).days
        # 当前日期至结束日期天数
        if (datetime.strptime(endtime, '%Y-%m-%d')-datetime.strptime(str(date.today()), '%Y-%m-%d')).days <= 0:
            processnow = 0
        else:processnow = (datetime.strptime(endtime, '%Y-%m-%d')-datetime.strptime(str(date.today()), '%Y-%m-%d')).days

        if processnow == 0:
            processpersen = 100
        else:processpersen = (1-round(processnow/processmax,3))*100
        warningday = request.form.get('warningday')


        conn = sqlite3.connect(DATABASE_URL)
        c = conn.cursor()
        sql0 = "select ROWID from ContractCreat WHERE ContractName = ?"
        sqlfind = c.execute(sql0,(contractname,)).fetchone()
        if sqlfind is not None:
            return render_template('500.html', tips ='合同名称已存在', back ='contract.contract_creat')
        else:
            sql = 'insert into ContractCreat (ContractName, StartTime, EndTime, Price, Stamp, ProcessMax, ProcessNow, ProcessPercen, WarningDay) values (?,?,?,?,?,?,?,?,?)'
            c.execute(sql, (contractname, starttime, endtime, price, stamp, processmax, processnow, processpersen, warningday))
            conn.commit()
            sql1 = "select ROWID,* from ContractCreat WHERE ContractName = ?"
            searchinfo = c.execute(sql1, (contractname,)).fetchone()
            conn.commit()
            conn.close()
            uploadpath = os.getcwd() + '/upload/{}'.format(searchinfo[0])
            if not os.path.exists(uploadpath):
                os.mkdir(uploadpath)
                return redirect(url_for('contract.contract_list'))
            else:
                return redirect(url_for('contract.contract_list'))



@contract.route('/upload/<id>/', methods=['GET', 'POST'])
def upload_file(id):
    uploadpath = os.getcwd() + '/upload/{}'.format(id)
    if request.method == 'POST':
        if not os.path.exists(uploadpath):
            os.mkdir(uploadpath)
            for f in request.files.getlist('file'):
                f.save(os.path.join(uploadpath, f.filename))
        else:
            for f in request.files.getlist('file'):
                f.save(os.path.join(uploadpath, f.filename))

        return render_template('index.html')



@contract.route('/del/<id>')
def contract_del(id = 0):
    conn = sqlite3.connect(DATABASE_URL)
    c= conn.cursor()
    sql = "delete from ContractCreat WHERE ROWID = ?"
    c.execute(sql,(id,))
    conn.commit()
    conn.close()

    files_list = os.listdir(os.getcwd() + '/upload/{}'.format(id))
    for filename in files_list:
        os.remove(os.getcwd() + '/upload/{}/{}'.format(id, filename))
    os.rmdir(os.getcwd() + '/upload/{}/'.format(id))

    return redirect(url_for('contract.contract_list'))

@contract.route('/edit/<id>/')
def contract_edit(id = 0):
    conn = sqlite3.connect(DATABASE_URL)
    c = conn.cursor()
    sql = "select ROWID,* from ContractCreat WHERE ROWID = ?"
    searchinfo = c.execute(sql, (id,)).fetchone()
    conn.commit()
    conn.close()
    return render_template('contract-edit.html', searchinfo = searchinfo)

@contract.route('/save_edit/', methods=['POST'])
def post_edit():
    if request.method == 'POST':
        rowid = request.form.get('rowid')
        starttime = request.form.get('starttime')
        endtime = request.form.get('endtime')
        price = request.form.get('price')
        stamp = datetime.now()
        processmax = (datetime.strptime(endtime, '%Y-%m-%d') - datetime.strptime(starttime, '%Y-%m-%d')).days
        # 当前日期至结束日期天数
        if (datetime.strptime(endtime, '%Y-%m-%d') - datetime.strptime(str(date.today()), '%Y-%m-%d')).days <= 0:
            processnow = 0
        else:
            processnow = (
            datetime.strptime(endtime, '%Y-%m-%d') - datetime.strptime(str(date.today()), '%Y-%m-%d')).days

        if processnow == 0:
            processpersen = 100
        else:
            processpersen = (1 - round(processnow / processmax, 3)) * 100
        warningday = request.form.get('warningday')

        conn = sqlite3.connect(DATABASE_URL)
        c = conn.cursor()
        sql = """update ContractCreat set
                                      StartTime = ?,
                                      EndTime = ?,
                                      Price = ?,
                                      WarningDay = ?,
                                      ProcessMax = ?,
                                      ProcessNow = ?,
                                      ProcessPercen = ?
                              WHERE rowid = ?"""

        c.execute(sql,
                  (starttime, endtime, price, warningday, processmax, processnow, processpersen, rowid))
        conn.commit()
        conn.close()
        return redirect(url_for('contract.contract_list'))



@contract.route('/list/')
def contract_list():
    conn =sqlite3.connect(DATABASE_URL)
    c= conn.cursor()
    sql = 'select ROWID,* from ContractCreat ORDER BY StartTime DESC '
    contractinfo = c.execute(sql).fetchall()
    conn.commit()
    conn.close()

    files={}
    for file in contractinfo:
        files_list = os.listdir(os.getcwd() + '/upload/{}'.format(file[0]))
        files[file[0]]=files_list

    return render_template('contract-list.html', items=contractinfo, files = files)


@contract.route('/delete/<id>/<filename>')
def delete_file(id, filename):
    os.remove(os.getcwd() + '/upload/{}/{}'.format(id, filename))
    return redirect(url_for('contract.contract_list'))

@contract.route('/download/<id>/<filename>')
def download_file(id,filename):
    path = os.getcwd() + '/upload/{}/'.format(id)
    response = make_response(send_from_directory(path, filename, as_attachment = True))
    response.headers["Content-Disposition"] = "attachment; filename*=utf-8''{}".format(filename.encode())
    return response



