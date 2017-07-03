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
    sql1 = "select rowid,* from Module ORDER BY rowid DESC "
    mod = c.execute(sql1).fetchall()
    conn.commit()
    conn.close()
    return render_template('moduletext.html', mods=mod)
@BSmodule.route('/save_module/',methods = ['GET','POST'])
def post_module():
    if request.method == 'POST':
        if request.form.get('mode') == 'add':
            servername = request.form.get('servername')
            insideip = request.form.get('insideip')
            insideport = request.form.get('insideport')
            outsideip = request.form.get('outsideip')
            outsideport = request.form.get('outsideport')
            area = request.form.get('area')

            conn = sqlite3.connect(DATABASE_URL)
            c = conn.cursor()
            sql = "insert into Module (ServerName, InsideIP, InsidePort, OutsideIP, OutsidePort, Area) VALUES (?,?,?,?,?,?)"
            c.execute(sql,
                      (servername, insideip, insideport, outsideip, outsideport, area))
            conn.commit()
            conn.close()
            return redirect(url_for('BSmodule.module_list'))
        elif request.form.get('mode') == 'update':
            rowid = request.form.get('rowid')
            servername = request.form.get('servername')
            insideip = request.form.get('insideip')
            insideport = request.form.get('insideport')
            outsideip = request.form.get('outsideip')
            outsideport = request.form.get('outsideport')
            area = request.form.get('area')

            conn = sqlite3.connect(DATABASE_URL)
            c = conn.cursor()
            sql = """update Module set
                            ServerName = ?,
                            InsideIP = ?,
                            InsidePort= ?,
                            OutsideIP= ?,
                            OutsidePort= ?,
                            Area= ?
                        WHERE rowid = ?"""
            c.execute(sql,
                      (servername, insideip, insideport, outsideip, outsideport, area, rowid))
            conn.commit()
            conn.close()
            return redirect(url_for('BSmodule.module_list'))
    elif request.method == 'GET':
        if request.args.get('mode') == 'delete':
            rowid = request.args.get('rowid')
            conn = sqlite3.connect(DATABASE_URL)
            c = conn.cursor()
            sql = """delete from Module WHERE rowid = ?"""
            c.execute(sql,
                      (rowid,))
            conn.commit()
            conn.close()
            return redirect(url_for('BSmodule.module_list'))

