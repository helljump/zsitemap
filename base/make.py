#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = "helljump"


from ZODB.FileStorage import FileStorage
from ZODB.DB import DB as ZDB
from BTrees.OOBTree import OOBTree
import transaction


storage = FileStorage('db/dict', read_only=False, pack_gc=True, pack_keep_old=False)
DB = ZDB(storage)
DB.pack()
CONN = DB.open()
root = CONN.root()
d = root['synonyms'] = OOBTree()
print len(d)
t = transaction.get()
for i, row in enumerate(open('ru_sinonim_morf270046.txt')):
    k, v = unicode(row, 'cp1251').split(',')
    d[k] = v
    if i % 10000 == 0:
        print i,
t.commit()
print len(d)
DB.undo(t)
print len(d)
CONN.close()
DB.pack()
DB.close()
storage.close()
