#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from ctypes import *
import logging
from bson import BSON
import re


log = logging.getLogger(__name__)


libtc = cdll.LoadLibrary('tcejdbdll.dll')


class COMPRESS():
    LARGE = 1 << 0  # /* use 64-bit bucket array */
    DEFLATE = 1 << 1  # /* compress each record with Deflate */
    BZIP = 1 << 2  # /* compress each record with BZIP2 */
    TCBS = 1 << 3  # /* compress each record with TCBS */
    TEXCODEC = 1 << 4  # /* compress each record with custom functions */


class WMODE():
    READER = 1 << 0  # /* open as a reader */
    WRITER = 1 << 1  # /* open as a writer */
    CREAT = 1 << 2  # /* writer creating */
    TRUNC = 1 << 3  # /* writer truncating */
    NOLCK = 1 << 4  # /* open without locking */
    LCKNB = 1 << 5  # /* lock without blocking */
    TSYNC = 1 << 6  # /* synchronize every transaction */


class tc_char_p(c_char_p):
    def __del__(self):
        if self and libtc:
            libtc.tcfree(self)

class tc_void_p(c_void_p):
    def __del__(self):
        if self and libtc:
            libtc.tcfree(self)


class TokyoHash():


    def __init__(self, fname, create=False):
        self.set_proto()
        self.db = libtc.tchdbnew()
        if create:
            mode = WMODE.WRITER | WMODE.CREAT
        else:
            mode = WMODE.READER
        #libtc.tchdbtune(self.db, 0, -1, -1, COMPRESS.DEFLATE)
        libtc.tchdbopen(self.db, fname, mode)

    def set_proto(self):
        libtc.tchdbopen.argtypes = [c_void_p, c_char_p, c_int]
        libtc.tchdbopen.restype = bool
        libtc.tchdbtune.argtypes = [c_void_p, c_ulonglong, c_int, c_int, c_uint]
        libtc.tchdbtune.restype = bool
        libtc.tchdbnew.restype = c_void_p
        libtc.tchdbvanish.argtypes = [c_void_p]
        libtc.tchdbvanish.restype = bool
        libtc.tchdbput2.argtypes = [c_void_p, c_char_p, c_char_p]
        libtc.tchdbput2.restype = bool
        libtc.tchdbput.argtypes = [c_void_p, c_char_p, c_int, c_char_p, c_int]
        libtc.tchdbput.restype = bool
        libtc.tchdbget2.argtypes = [c_void_p, c_char_p]
        libtc.tchdbget2.restype = tc_char_p
        libtc.tchdbget.argtypes = [c_void_p, c_char_p, c_int, POINTER(c_int)]
        libtc.tchdbget.restype = tc_void_p
        libtc.tchdbsync.argtypes = [c_void_p]
        libtc.tchdbsync.restype = bool
        libtc.tchdbrnum.argtypes = [c_void_p]
        libtc.tchdbrnum.restype = c_ulonglong
        libtc.tchdbclose.argtypes = [c_void_p]
        libtc.tchdbclose.restype = bool
        libtc.tcfree.argtypes = [c_void_p]

    def vanish(self):
        return libtc.tchdbvanish(self.db)

    def put(self, k, v):
        assert isinstance(k, unicode)
        assert isinstance(v, unicode)
        return libtc.tchdbput2(self.db, str(k.encode('utf-8')), str(v.encode('utf-8')))

    def putbson(self, k, v):
        assert isinstance(k, unicode)
        assert isinstance(v, dict)
        raw_k = str(k.encode('utf-8'))
        raw_v = str(BSON.encode(v))
        return libtc.tchdbput(self.db, raw_k, len(raw_k), raw_v, len(raw_v))

    def get(self, k):
        assert isinstance(k, unicode)
        v = libtc.tchdbget2(self.db, str(k.encode('utf-8')))
        if v:
            return v.value.decode('utf-8')

    def getbson(self, k):
        assert isinstance(k, unicode)
        raw_k = str(k.encode('utf-8'))
        size = c_int(0)
        v = libtc.tchdbget(self.db, raw_k, len(raw_k), byref(size))
        if v:
            b = BSON(string_at(v.value, size))
            return b.decode()

    def sync(self):
        return libtc.tchdbsync(self.db)

    def __len__(self):
        return libtc.tchdbrnum(self.db)

    def close(self):
        return libtc.tchdbclose(self.db)


def create_dict():
    tc = TokyoHash('syno.tcn', True)
    for i, row in enumerate(open(r'd:\work2014\zsitemap\base\ru_sinonim_morf270046.txt')):
        k, v = unicode(row, 'cp1251').split(',')
        k = k.strip()
        v = v.strip()
        tc.put(k, v)
        if i % 10000 == 0:
            print i,
    tc.close()


def test_dict():
    c = 0
    tc = TokyoHash('syno.tcn')
    for i, row in enumerate(open(r'd:\work2014\zsitemap\base\ru_sinonim_morf270046.txt')):
        k, v = unicode(row, 'cp1251').split(',')
        v = tc.get(k),
        if v is not None:
            c += 1
        if i % 10000 == 0:
            print i,
    print 'founded', c
    tc.close()


def clean(word):
    return re.sub("\(.+?\)", "", word).strip().lower()


def make_thes():

    '''
    obj = {"b": u"пам парам", 'a': "2", 'c':[12,3,4]}
    b = BSON.encode(obj)
    print b
    open('test.bin', 'wb').write(b)
    print BSON.decode(b)
    return
    '''

    curline = 1
    subline = 0

    tc = TokyoHash('thes.tcn', True)
    with open(r'd:\work\cm2\src\edit\morph\th_ru_RU_v2.dat') as finp:
        lns = finp.readlines()
        encoding = lns.pop(0).strip()
        print "encoding:", encoding
        while lns:
            word, cnt = lns.pop(0).split("|")
            word = unicode(word, encoding).lower()
            cnt = int(cnt)
            vals = {'syn': set(), 'ant': set()}
            curline += 1
            subline += 1
            for i in range(cnt):
                egg = unicode(lns.pop(0), encoding).upper()
                spam = re.search('\(([\w\s]+)\)([\w\s\|]+)', egg, re.U)
                wtype = spam.group(1)
                therms = spam.group(2).split("|")
                therms = map(clean, therms)
                therms = [t for t in therms if len(t)]
                if wtype == u"СИНОНИМ":
                    vals['syn'] |= set(therms)
                elif wtype == u"АНТОНИМ":
                    vals['ant'] |= set(therms)
                elif wtype == u"СХОДНЫЙ ТЕРМИН":
                    vals['syn'] |= set(therms)
                elif wtype == u"СВЯЗАННЫЙ ТЕРМИН":
                    vals['syn'] |= set(therms)
                else:
                    raise Exception("unknown wtype %i" % curline)
                curline += 1
            vals['syn'] = list(vals['syn'])
            vals['ant'] = list(vals['ant'])
            #if word == u'бережный':
            #    print word, '->', '#'.join(vals['syn'])
            #    print word, '->', '#'.join(vals['ant'])
            assert tc.putbson(word, vals)
    tc.close()


if __name__ == '__main__':
    create_dict()
    #test_dict()
    make_thes()
    #tc = TokyoHash('thes.tcn')
    #v = '#'.join(tc.getbson(u'бережный')['syn'])
    #print v
    #tc.close()
