import os
import sqlite3
from flask import render_template,request,redirect,url_for
from datetime import datetime, date
from app.chart import chart

DATABASE_URL = os.path.realpath('./db/contract.db')

@chart.route('/cdn/')
def cdnchart():
    return render_template('data_table.html')

@chart.route('/cdn/creat/')
def creat_cdnchart():
    return render_template('creat-cdnchart.html')

@chart.route('/cdn/creat_post/',methods=['POST'])
def cdnchart_post():
    if request.method == 'POST':
        cdnname = request.form.get('cdnname')
        date_time = request.form.get('datetime')
        price = request.form.get('price')
        nightfive = request.form.get('nightfive')
        state = request.form.get('state')
        stamp = datetime.now()

        conn = sqlite3.connect(DATABASE_URL)
        c = conn.cursor()
        sql = 'insert into CDNTable (CdnName,Date_Time,Price, NightFive, State, Stamp) values (?,?,?,?,?,?)'
        c.execute(sql,
                  (cdnname, date_time, price, nightfive, state, stamp))
        conn.commit()
        conn.close()
        return redirect(url_for('chart.cdntable'))

@chart.route('/cdn/table/')
def cdntable():
    conn = sqlite3.connect(DATABASE_URL)
    c = conn.cursor()
    sql = 'select ROWID,* from CDNTable ORDER BY cdnname,Date_Time DESC '
    cdninfo = c.execute(sql).fetchall()
    conn.commit()
    conn.close()
    return render_template('data_table.html', cdninfo = cdninfo)

@chart.route('/cdn/del/<id>')
def cdndel(id):
    conn = sqlite3.connect(DATABASE_URL)
    c = conn.cursor()
    sql = 'delete from CDNTable WHERE rowid = ?'
    c.execute(sql,(id,))
    conn.commit()
    conn.close()
    return redirect(url_for('chart.cdntable'))

@chart.route('/cdn/edit/<id>')
def cdnedit(id):
    conn = sqlite3.connect(DATABASE_URL)
    c = conn.cursor()
    sql = 'select rowid,* from CDNTable WHERE rowid = ?'
    cdninfo = c.execute(sql, (id,)).fetchone()
    conn.commit()
    conn.close()
    return render_template('cdnchart-edit.html',cdninfo = cdninfo)

@chart.route('/cdn/save_edit/',methods = ['POST'])
def save_edit():
    rowid = request.form.get('rowid')
    cdnname = request.form.get('cdnname')
    date_time = request.form.get('datetime')
    price = request.form.get('price')
    nightfive = request.form.get('nightfive')
    state = request.form.get('state')

    conn = sqlite3.connect(DATABASE_URL)
    c = conn.cursor()
    sql = """update CDNTable set
                                          CdnName = ?,
                                          Date_Time = ?,
                                          Price = ?,
                                          NightFive = ?,
                                          State = ?
                                  WHERE rowid = ?"""
    c.execute(sql,
              (cdnname, date_time, price, nightfive, state, rowid))
    conn.commit()
    conn.close()
    return redirect(url_for('chart.cdntable'))

@chart.route('/cdn/chart/')
def chart_cdn():
    conn = sqlite3.connect(DATABASE_URL)
    c = conn.cursor()
    sql = "select Date_Time,Price,CdnName from CDNTable ORDER BY Date_Time"
    result = c.execute(sql).fetchall()
    info = []
    for i in result:
        for dict_tmp in info:
            if dict_tmp.get('name', '') == i[2]:
                dict_tmp['data'].append([i[0], i[1]])
                break
        else:
            info.append(
                {
                    'name': i[2],
                    'data': [[i[0], i[1]]]
                }
            )

    return render_template('cdnchart.html',info = info)

@chart.route('/cdn/test/')
def chart_test():


    return render_template('test4.html')

@chart.route('/cdn/content/')
def content():
    return str(datetime.now())



