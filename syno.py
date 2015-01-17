#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = 'helljump'

import logging
import startup
import re
from PyQt4 import QtCore, QtGui
from ui.syno_ui import Ui_SynoDialog
import tokyohash


log = logging.getLogger(__name__)


NONWORDS = re.compile(r'(\W+)', re.U | re.I)
LIMIT = 6


class SynoDialog(QtGui.QDialog, Ui_SynoDialog):

    def __init__(self, parent=None):
        super(SynoDialog, self).__init__(parent)
        self.setupUi(self)
        startup.CFG.beginGroup('syno')
        try:
            if startup.CFG.value('title', True, type=bool):
                self.title_cb.setCheckState(QtCore.Qt.Checked)
            if startup.CFG.value('description', True, type=bool):
                self.description_cb.setCheckState(QtCore.Qt.Checked)
        except TypeError:
            log.debug('set defaults')
            self.title_cb.setCheckState(QtCore.Qt.Checked)
            self.description_cb.setCheckState(QtCore.Qt.Checked)
        startup.CFG.endGroup()

    def accept(self):
        startup.CFG.beginGroup('syno')
        startup.CFG.setValue('title', self.title_cb.checkState() == QtCore.Qt.Checked)
        startup.CFG.setValue('description', self.description_cb.checkState() == QtCore.Qt.Checked)
        startup.CFG.endGroup()
        super(SynoDialog, self).accept()


class Syno():

    def __init__(self):
        #self.syno = startup.CONN.root()['syno']
        self.syno = tokyohash.TokyoHash('syno.tcn')

    def __call__(self, text):
        sp = NONWORDS.split(text)
        ou = []
        i = 0
        while i < len(sp):
            for j in range(LIMIT, 0, -1):
                k = ''.join(sp[i:i+j])
                v = self.syno.get(k.lower())
                if v is not None:
                    if k.istitle():
                        v = v.capitalize()
                    elif k.isupper():
                        v = v.upper()
                    elif k.islower():
                        v = v.lower()
                    ou.append(v)
                    i += j
                    break
            else:
                ou.append(sp[i])
                i += 1
        return ''.join(ou)

    def __del__(self):
        self.syno.close()
        log.debug('close cabinet')


def main():
    s = Syno()
    #print s(u'Как заявил президент России, пока нет сведений о том, что злого произойдет в будущем.')
    print s(u'Небесный | zipta')
    print s(u'небесный')

if __name__ == '__main__':
    main()
