#-*-coding:utf-8-*-
import pymysql


db=pymysql.connect(user='root',password='mysqlmm',host='localhost',port=3306,db='spider')
cursor=db.cursor()
sql='SELECT * FROM student WHERE age>20'
try:
    cursor.execute(sql)
    one=cursor.fetchone()
    while one:
        print(one)
        one = cursor.fetchone()
    '''cursor.execute(sql)
    print('count:',cursor.rowcount)
    one=cursor.fetchone()
    print(one)
    results=cursor.fetchall()
    print(results)
    for i in results:
        print(i)'''
except:
    print('error')