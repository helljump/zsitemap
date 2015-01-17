# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scripts.ui'
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

class Ui_ScriptsDialog(object):
    def setupUi(self, ScriptsDialog):
        ScriptsDialog.setObjectName(_fromUtf8("ScriptsDialog"))
        ScriptsDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ScriptsDialog.resize(714, 480)
        self.gridLayout = QtGui.QGridLayout(ScriptsDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(ScriptsDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tree_tv = QtGui.QTreeView(self.splitter)
        self.tree_tv.setMaximumSize(QtCore.QSize(191, 16777215))
        self.tree_tv.setObjectName(_fromUtf8("tree_tv"))
        self.frame = QtGui.QFrame(self.splitter)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.script_sc = Qsci.QsciScintilla(self.frame)
        self.script_sc.setToolTip(_fromUtf8(""))
        self.script_sc.setWhatsThis(_fromUtf8(""))
        self.script_sc.setObjectName(_fromUtf8("script_sc"))
        self.gridLayout_2.addWidget(self.script_sc, 0, 0, 1, 4)
        self.start_pb = QtGui.QPushButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/control_play_blue.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_pb.setIcon(icon)
        self.start_pb.setObjectName(_fromUtf8("start_pb"))
        self.gridLayout_2.addWidget(self.start_pb, 1, 2, 1, 2)
        self.gridLayout.addWidget(self.splitter, 0, 1, 1, 1)
        self.actionGroup = QtGui.QAction(ScriptsDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGroup.setIcon(icon1)
        self.actionGroup.setObjectName(_fromUtf8("actionGroup"))
        self.actionItem = QtGui.QAction(ScriptsDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/script.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItem.setIcon(icon2)
        self.actionItem.setObjectName(_fromUtf8("actionItem"))
        self.actionRemove = QtGui.QAction(ScriptsDialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove.setIcon(icon3)
        self.actionRemove.setObjectName(_fromUtf8("actionRemove"))

        self.retranslateUi(ScriptsDialog)
        QtCore.QMetaObject.connectSlotsByName(ScriptsDialog)

    def retranslateUi(self, ScriptsDialog):
        ScriptsDialog.setWindowTitle(_translate("ScriptsDialog", "Макросы", None))
        self.start_pb.setText(_translate("ScriptsDialog", "Старт", None))
        self.actionGroup.setText(_translate("ScriptsDialog", "Добавить группу", None))
        self.actionItem.setText(_translate("ScriptsDialog", "Добавить скрипт", None))
        self.actionRemove.setText(_translate("ScriptsDialog", "Удалить", None))

from PyQt4 import Qsci
import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ScriptsDialog = QtGui.QDialog()
    ui = Ui_ScriptsDialog()
    ui.setupUi(ScriptsDialog)
    ScriptsDialog.show()
    sys.exit(app.exec_())

