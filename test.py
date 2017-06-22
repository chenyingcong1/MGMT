import sqlite3,os
import pandas as pd

DATABASE_URL = os.path.realpath('./db/contract.db')
con = sqlite3.connect(DATABASE_URL)
c = con.cursor()
sql = "select * from Module"
# df =pd.read_sql(sql,con,index_col='Date_Time,Price,CdnName')
mod = c.execute(sql).fetchall()
con.commit()
con.close()
lis = [
        ['Location','Parent','Market trade volume (size)','Market increase/decrease (color)'],
        ['Global','',0,0],
        ]
for i in mod:
    count = 5
    if [i[0],'Global',0,0] not in lis:
        lis.append([i[0],'Global',0,0])
    else:pass
    if ['{}-{}'.format(i[0],i[1]),i[0],count,count] not in lis:
        lis.append(['{}-{}'.format(i[0],i[1]),i[0],count,count])
        count = count+5

    else:pass

    lis.append([i[2],'{}-{}'.format(i[0],i[1]),count,count])




# print(lis)
# print(mod)
[['Location', 'Parent', 'Market trade volume (size)', 'Market increase/decrease (color)'],
 ['Global', '', 0, 0],
 ['听云监测', 'Global', 0, 0],
 ['听云监测-BA', '听云监测', 5, 5],
 ['172.16.101.31', '听云监测-BA', 10, 10],
 ['172.16.101.32', '听云监测-BA', 5, 5],
 ['听云监测1', 'Global', 0, 0],
 ['听云监测1-BA', '听云监测1', 5, 5],
 ['172.16.101.33', '听云监测1-BA', 10, 10],
 ['听云监测1-APP', '听云监测1', 5, 5],
 ['172.16.101.34', '听云监测1-APP', 10, 10],
 ['听云监测2', 'Global', 0, 0],
 ['听云监测2-APP', '听云监测2', 5, 5],
 ['172.16.101.35', '听云监测2-APP', 10, 10],
 ['172.16.101.36', '听云监测2-APP', 5, 5]]



import os
import paramiko
import datetime

path = '/root'
ip = '172.16.7.52'
client = paramiko.Transport((ip,22))
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(username='root',password='cutv@sobey2016')
sftp = paramiko.SFTPClient.from_transport(client)
files = sftp.listdir_attr(path)
print(files)

[<SFTPAttributes: [ size=18 uid=0 gid=0 mode=0o100644 atime=1489741977 mtime=1388283991 ]>,
<SFTPAttributes: [ size=176 uid=0 gid=0 mode=0o100644 atime=1498125571 mtime=1388283991 ]>,
<SFTPAttributes: [ size=176 uid=0 gid=0 mode=0o100644 atime=1498125571 mtime=1388283991 ]>,
<SFTPAttributes: [ size=100 uid=0 gid=0 mode=0o100644 atime=1388283991 mtime=1388283991 ]>,
<SFTPAttributes: [ size=129 uid=0 gid=0 mode=0o100644 atime=1388283991 mtime=1388283991 ]>,
<SFTPAttributes: [ size=954 uid=0 gid=0 mode=0o100600 atime=1466667773 mtime=1466667773 ]>,
<SFTPAttributes: [ size=3412 uid=0 gid=0 mode=0o100600 atime=1498125832 mtime=1498125687 ]>,
<SFTPAttributes: [ size=27 uid=0 gid=0 mode=0o40755 atime=1489768815 mtime=1489740080 ]>,
<SFTPAttributes: [ size=17 uid=0 gid=0 mode=0o40755 atime=1489768815 mtime=1480926483 ]>,
<SFTPAttributes: [ size=18 uid=0 gid=0 mode=0o40740 atime=1489768815 mtime=1489737919 ]>,
<SFTPAttributes: [ size=24 uid=0 gid=0 mode=0o40700 atime=1489905417 mtime=1489905441 ]>,
<SFTPAttributes: [ size=16 uid=0 gid=0 mode=0o40755 atime=1489909691 mtime=1489909691 ]>,
<SFTPAttributes: [ size=34 uid=0 gid=0 mode=0o40755 atime=1498128371 mtime=1498128370 ]>,
<SFTPAttributes: [ size=20 uid=0 gid=0 mode=0o100644 atime=1498127614 mtime=1498127594 ]>,
<SFTPAttributes: [ size=3895 uid=0 gid=0 mode=0o100600 atime=1498128370 mtime=1498128370 ]>]


# print(files)
# for f in files:
#     if list(f)[0] is ".":
#         pass
    # else:print(f)




# client.connect('172.16.7.52', 22, username='root', password='cutv@sobey2016', timeout=4)
# stdin, stdout, stderr = client.exec_command('ls -l')
# for std in stdout.readlines():
#   print (std,)
# client.close()



