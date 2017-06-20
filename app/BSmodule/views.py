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
    sql2 = "SELECT rowid,ModuleName FROM MODULE GROUP BY ModuleName HAVING COUNT(*) >= 1 "
    mod = c.execute(sql1).fetchall()
    modname = c.execute(sql2).fetchall()
    conn.commit()
    conn.close()
    lis = [['Location', 'Parent', 'Market trade volume (size)', 'Market increase/decrease (color)'],
           ['Global', str('null'), 0, 0]]
    for i in mod:
        lis.append([i[0], 'Global', 0, 0])
        lis.append([i[1], i[0], 5, 5])
        lis.append(['内网IP:{}:{}-外网IP{}:{}'.format(i[2], i[3], i[4], i[5]), i[1], 20, 20])
    # dict_tmp = []
    # for i in mod:
    #     id = 0
    #     for s in dict_tmp:
    #         if s['name'] == i[0]:
    #             if i[1] not in s['server'][0][0]:
    #                 s['server'].append([i[1], i[2], [i[3]], [i[4]], [i[5]]])
    #
    #
    #     else:
    #         dict_tmp.append(
    #             {
    #                 'id': random.randint(0, 10000),
    #                 'name': i[0],
    #                 'server': [[i[1], [i[2]], [i[3]], [i[4]], [i[5]]]]
    #             }
    #         )

    return render_template('module.html', mods=lis)
    # return modules[0][3]
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
