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




import paramiko
from stat import S_ISDIR



client = paramiko.Transport(('10.20.100.86',50289))
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(username='root',password='1vu~Teh*(*eELuK23yd(YTG')
sftp = paramiko.SFTPClient.from_transport(client)
# def find_filename(remote_file=0,remote_dir=0):
#     if remote_dir == 0:
#         path = '/data/vod7'
#     else:
#         path = remote_dir
#     files = sftp.listdir_attr(path)
#     for f in files:
#         filename = path + '/' + f.filename
#         if list(f.filename)[0] is ".":
#             pass
#         elif S_ISDIR(f.st_mode):
#             find_filename(remote_file,filename)
#             print(filename)
#         elif remote_file in f.filename:
#             # print(filename)
#             pass
# find_filename(remote_file='G14efeekgfimhigmjmnmcv_1b.jpg')


a = [1]
if a:
    print('yes')
else:print('no')







# client.connect('172.16.7.52', 22, username='root', password='cutv@sobey2016', timeout=4)
# stdin, stdout, stderr = client.exec_command('ls -l')
# for std in stdout.readlines():
#   print (std,)
# client.close()



