# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Thu Mar 13 09:17:11 2014
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

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AboutDialog.resize(483, 225)
        self.gridLayout = QtGui.QGridLayout(AboutDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(AboutDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.ver_le = QtGui.QLabel(AboutDialog)
        self.ver_le.setObjectName(_fromUtf8("ver_le"))
        self.gridLayout.addWidget(self.ver_le, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(AboutDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.hw_le = QtGui.QLineEdit(AboutDialog)
        self.hw_le.setReadOnly(True)
        self.hw_le.setObjectName(_fromUtf8("hw_le"))
        self.gridLayout.addWidget(self.hw_le, 3, 1, 1, 1)
        self.label = QtGui.QLabel(AboutDialog)
        self.label.setMaximumSize(QtCore.QSize(202, 209))
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/aaaa.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 4, 1)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(_translate("AboutDialog", "О программе", None))
        self.label_3.setText(_translate("AboutDialog", "<html><head/><body><p><span style=\" font-size:18pt;\">ZSiteMap</span></p></body></html>", None))
        self.ver_le.setText(_translate("AboutDialog", "build", None))
        self.label_2.setText(_translate("AboutDialog", "<html><head/><body><hr/><p><span style=\" font-size:10pt;\">Сайт: </span><a href=\"http://zipta.ru\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#0000ff;\">http://zipta.ru</span></a></p><p><span style=\" font-size:10pt;\">ICQ: </span><span style=\" font-size:10pt; font-weight:600;\">125521555</span></p></body></html>", None))
        self.hw_le.setText(_translate("AboutDialog", "hwdata", None))
        self.hw_le.setPlaceholderText(_translate("AboutDialog", "траляля", None))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AboutDialog = QtGui.QDialog()
    ui = Ui_AboutDialog()
    ui.setupUi(AboutDialog)
    AboutDialog.show()
    sys.exit(app.exec_())

