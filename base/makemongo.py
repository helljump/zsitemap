#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = "helljump"


import pymongo
c = pymongo.MongoClient()

db = c.zsitemap
syno = db.syno

for i, row in enumerate(open('ru_sinonim_morf270046.txt')):
    k, v = unicode(row, 'cp1251').split(',')
    syno.insert({
        'src': k,
        'dst': v
    })
    if i % 10000 == 0:
        print i,

c.close()
