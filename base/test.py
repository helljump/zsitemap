#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = "helljump"


from ZODB.FileStorage import FileStorage
from ZODB.DB import DB as ZDB


storage = FileStorage('db/dict', read_only=True)
DB = ZDB(storage)
CONN = DB.open()
root = CONN.root()
d = root['synonyms']

print d[u'небесный']
print d[u'11']

CONN.close()
DB.close()
storage.close()
