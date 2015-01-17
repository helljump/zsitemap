# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query.ui'
#
# Created: Thu Mar 13 09:17:12 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QueryDialog(object):
    def setupUi(self, QueryDialog):
        QueryDialog.setObjectName(_fromUtf8("QueryDialog"))
        QueryDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        QueryDialog.resize(609, 375)
        self.gridLayout = QtGui.QGridLayout(QueryDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.links_te = QtGui.QPlainTextEdit(QueryDialog)
        self.links_te.setObjectName(_fromUtf8("links_te"))
        self.gridLayout.addWidget(self.links_te, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(QueryDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.label = QtGui.QLabel(QueryDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(QueryDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QueryDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QueryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QueryDialog)

    def retranslateUi(self, QueryDialog):
        QueryDialog.setWindowTitle(_translate("QueryDialog", "Ссылки на карты", None))
        self.label.setText(_translate("QueryDialog", "<html><head/><body><p>Укажите построчно ссылки на карты сайтов для парсинга. Например: http://zipta.ru/sitemap.xml</p></body></html>", None))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QueryDialog = QtGui.QDialog()
    ui = Ui_QueryDialog()
    ui.setupUi(QueryDialog)
    QueryDialog.show()
    sys.exit(app.exec_())

