#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = 'helljump'

import logging
from PyQt4 import QtCore, QtGui
from ui.prefs_ui import Ui_PrefsDialog
import startup


log = logging.getLogger(__name__)


TEMPLATE = '{{ title }}|{{ link }}|{{ description }}'


class HighLighter(QtGui.QSyntaxHighlighter):

    def __init__(self, doc):
        super(HighLighter, self).__init__(doc)
        self.color = QtGui.QTextCharFormat()
        self.color.setFontWeight(QtGui.QFont.Bold)
        self.color.setForeground(QtCore.Qt.darkCyan)
        self.expression = QtCore.QRegExp("(\{\{.+\}\})|(\{#.+#\})|(\{%.+%\})", syntax=QtCore.QRegExp.RegExp)
        self.expression.setMinimal(True)

    def highlightBlock(self, text):
        index = self.expression.indexIn(text)
        while index >= 0:
            length = self.expression.matchedLength()
            self.setFormat(index, length, self.color)
            index = self.expression.indexIn(text, index + length)


class PrefsDialog(QtGui.QDialog, Ui_PrefsDialog):
    def __init__(self, parent=None):
        super(PrefsDialog, self).__init__(parent)
        self.setupUi(self)
        HighLighter(self.template_te.document())
        startup.CFG.beginGroup('prefs')
        if startup.CFG.contains('geometry'):
            self.restoreGeometry(startup.CFG.value('geometry').toByteArray())
        try:
            self.template_te.setPlainText(startup.CFG.value('template', type=unicode))
            self.threads_sb.setValue(startup.CFG.value('threads', type=int))
            self.maximum_sb.setValue(startup.CFG.value('maximum', type=int))
            self.pause_sb.setValue(startup.CFG.value('pause', type=int))
        except TypeError:
            self.reset()
        startup.CFG.endGroup()

    def reset(self):
        log.debug('set defaults')
        self.template_te.setPlainText(TEMPLATE)
        self.threads_sb.setValue(3)
        self.maximum_sb.setValue(2000)
        self.pause_sb.setValue(0)

    def save(self):
        startup.CFG.beginGroup('prefs')
        startup.CFG.setValue('pause', self.pause_sb.value())
        startup.CFG.setValue('threads', self.threads_sb.value())
        startup.CFG.setValue('maximum', self.maximum_sb.value())
        startup.CFG.setValue('template', unicode(self.template_te.toPlainText()))
        startup.CFG.endGroup()

    def clickedBB(self, btn):
        role = self.buttonBox.buttonRole(btn)
        if role == QtGui.QDialogButtonBox.AcceptRole:
            log.debug('save')
            self.save()
            self.close()
        elif role == QtGui.QDialogButtonBox.RejectRole:
            log.debug('cancel')
            self.close()
        elif role == QtGui.QDialogButtonBox.ResetRole:
            log.debug('reset')
            self.reset()

    def closeEvent(self, evt):
        log.debug('close')
        startup.CFG.beginGroup('prefs')
        startup.CFG.setValue('geometry', self.saveGeometry())
        startup.CFG.endGroup()
        evt.accept()


if __name__ == '__main__':
    dlg = PrefsDialog()
    startup.SPLASH.finish(dlg)
    dlg.exec_()
