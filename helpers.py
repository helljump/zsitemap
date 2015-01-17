#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = 'helljump'

import logging
from PyQt4 import QtCore
from PyQt4 import QtGui
from ui import icons_rc  # noqa
from persistent import Persistent


log = logging.getLogger(__name__)


class Link(Persistent):

    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description

    def __eq__(self, other):
        return cmp(self.url, other.url) == 0

    def set_title(self, text_utf):
        self.title = unicode(text_utf, 'utf8')


class MySplash(QtGui.QSplashScreen):
    def __init__(self):
        pm = QtGui.QPixmap(":/aaaa.png")
        super(MySplash, self).__init__(pm)

    def message(self, s):
        self.showMessage(s, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop, QtCore.Qt.white)
        QtGui.qApp.processEvents()


class MyProgressDialog(QtGui.QProgressDialog):

    closed = QtCore.pyqtSignal()

    def __init__(self, title, label, cancel, from_=0, to=0, parent=None):
        super(MyProgressDialog, self).__init__(label, cancel, from_, to, parent)
        self.setWindowTitle(title)
        self.setModal(True)
        self.setFixedWidth(400)

    def set_text(self, text):
        self.setLabelText(text)

    def inc_value(self, v=1):
        self.setValue(self.value() + v)

    def set_range(self, from_, to):
        self.pdlg.setRange(from_, to)
        self.pdlg.setValue(from_)

    def inc_range(self, by=1):
        self.pdlg.setMaximum(self.pdlg.maximum() + by)

    def hideEvent(self, evt):
        log.debug('emit close')
        self.closed.emit()
        evt.accept()
