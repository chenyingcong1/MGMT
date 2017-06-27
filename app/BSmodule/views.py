import os,random
import sqlite3
from flask import render_template,request,redirect,url_for
from datetime import datetime, date
from app.BSmodule import BSmodule

DATABASE_URL = os.path.realpath('./db/contract.db')

@BSmodule.route('/module/list/')
def module_list():
    conn = sqlite3.connect(DATABASE_URL)
    c = conn.cursor()
    sql1 = "select * from Module"
    mod = c.execute(sql1).fetchall()
    conn.commit()
    conn.close()
    return render_template('module.html', mods=mod)
@BSmodule.route('/save_module/',methods = ['POST'])
def post_module():
    if request.method == 'POST':
        modulename = request.form.get('modulename')
        servername = request.form.get('servername')
        insideip = str(request.form.get('insideip')).replace(',','<br/>')
        insideport = request.form.get('insideport')
        outsideip = str(request.form.get('outsideip')).replace(',', '<br/>')
        outsideport = request.form.get('outsideport')

        conn = sqlite3.connect(DATABASE_URL)
        c = conn.cursor()
        sql = "insert into Module (ServerName, ModuleName, InsideIP, InsidePort, OutsideIP, OutsidePort) VALUES (?,?,?,?,?,?)"
        c.execute(sql,
                  (servername,modulename,insideip,insideport,outsideip,outsideport))
        conn.commit()
        conn.close()
        return redirect(url_for('BSmodule.module_list'))
