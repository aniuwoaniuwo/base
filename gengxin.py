#-*-coding:utf-8-*-
'''
插入数据
import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
db.close()
'''
import pymysql

data={
    'id':'1157',
    'name':'tony3',
    'age':22
}
db=pymysql.connect(host='localhost',user='root',password='mysqlmm',port=3306,db='spider')
cursor=db.cursor()
table='student'
keys=','.join(data.keys())
values=','.join(['%s']*len(data))

sql = 'INSERT INTO {table}({keys})VALUES({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values)
update = ','.join([" {key}= %s".format(key=key) for key in data])#要注意空格
sql = sql+update
#sql='UPDATE student SET age=%s WHERE name=%s'
try:
    if cursor.execute(sql,tuple(data.values())*2):
    #if cursor.execute(sql,(21,'tony')):
        print('successful')
        db.commit()
except:
    print('failed')
    db.rollback()
db.close()