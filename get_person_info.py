#! -*- coding=utf-8 -*-
u"""获取所有的个人信息文件"""
import sqlite3
import os

sc = sqlite3.connect('db.sqlite3')
rows = sc.execute('select shop_num, staff_code from users_user')

for row in rows:
    if not os.path.exists('person_info/%s/%s/' % (row[0], row[1])):
        os.mkdir('person_info/%s/%s' % (row[0], row[1]))
    os.system('curl http://myy-a2015e8014661092.c9users.io/person_info/%s/%s/ -o person_info/%s/%s/index.html' % (row[0], row[1], row[0], row[1]))

sc.close()
