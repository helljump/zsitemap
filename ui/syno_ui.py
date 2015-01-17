# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'syno.ui'
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

class Ui_SynoDialog(object):
    def setupUi(self, SynoDialog):
        SynoDialog.setObjectName(_fromUtf8("SynoDialog"))
        SynoDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        SynoDialog.resize(289, 129)
        self.gridLayout_4 = QtGui.QGridLayout(SynoDialog)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.buttonBox = QtGui.QDialogButtonBox(SynoDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_4.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.description_cb = QtGui.QCheckBox(SynoDialog)
        self.description_cb.setObjectName(_fromUtf8("description_cb"))
        self.gridLayout_4.addWidget(self.description_cb, 1, 0, 1, 1)
        self.title_cb = QtGui.QCheckBox(SynoDialog)
        self.title_cb.setObjectName(_fromUtf8("title_cb"))
        self.gridLayout_4.addWidget(self.title_cb, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 0, 1, 1)

        self.retranslateUi(SynoDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SynoDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SynoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SynoDialog)

    def retranslateUi(self, SynoDialog):
        SynoDialog.setWindowTitle(_translate("SynoDialog", "Синонимы", None))
        self.description_cb.setText(_translate("SynoDialog", "Обработка описания", None))
        self.title_cb.setText(_translate("SynoDialog", "Обработка заголовков", None))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SynoDialog = QtGui.QDialog()
    ui = Ui_SynoDialog()
    ui.setupUi(SynoDialog)
    SynoDialog.show()
    sys.exit(app.exec_())

