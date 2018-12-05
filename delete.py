#-*-coding:utf-8-*-
import pymysql

db=pymysql.connect(host='localhost',user='root',password='mysqlmm',port=3306,db='spider')
cursor=db.cursor()
table='student'
condition='age > 20'
sql='DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
try:
    if cursor.execute(sql):
    #if cursor.execute(sql,(21,'tony')):
        print('successful')
        db.commit()
except:
    print('failed')
    db.rollback()
db.close()