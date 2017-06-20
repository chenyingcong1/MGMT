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
       ['cutv','',0]]
for  i in mod:
    if [i[0],'Global',0] not in lis:
        lis.append([i[0],'Global',0])
    else:
        pass
    if [i[1],i[0],5,5] not in lis:
        lis.append([i[1],i[0],5])
    else:
        pass
    lis.append(['内网IP:{}:{}-外网IP{}:{}'.format(i[2],i[3],i[4],i[5]),i[1],20])


print(lis)

# df = pd.DataFrame(data_input)
# df.columns = ['month','value','name']
# d = df.set_index(['month'])
# print ( set(d.index) )                           # {'张三', '李四'}
# print ( list(d.loc['张三'].values.tolist()) )  # data變成list
# print ( [{'data':list(d.loc[x].values.tolist()) , 'name': x} for x in set(d.index) ] )


