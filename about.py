#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = 'helljump'

import logging
from PyQt4 import QtGui
import startup
from ui.about_ui import Ui_AboutDialog
from win32api import GetFileVersionInfo, LOWORD, HIWORD
import sys


log = logging.getLogger(__name__)


class AboutDialog(QtGui.QDialog, Ui_AboutDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        try:
            m = __import__('BUILD_CONSTANTS')
            #info = GetFileVersionInfo(sys.executable, "\\")
            #ms = info['FileVersionMS']
            #ls = info['FileVersionLS']
            #egg = HIWORD(ms), LOWORD(ms), HIWORD(ls), LOWORD(ls)
            #self.ver_le.setText('.'.join(map(str, egg)))
            self.ver_le.setText(m.BUILD_TIMESTAMP)
        except ImportError, err:
            log.debug('%s', err)
        self.hw_le.setText(startup.HWINFO)


if __name__ == '__main__':
    dlg = AboutDialog()
    startup.SPLASH.finish(dlg)
    dlg.exec_()
