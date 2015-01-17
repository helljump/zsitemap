# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'links.ui'
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

class Ui_LinksWindow(object):
    def setupUi(self, LinksWindow):
        LinksWindow.setObjectName(_fromUtf8("LinksWindow"))
        LinksWindow.resize(918, 675)
        LinksWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtGui.QWidget(LinksWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.table_tv = QtGui.QTableView(self.centralwidget)
        self.table_tv.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table_tv.setAlternatingRowColors(True)
        self.table_tv.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_tv.setObjectName(_fromUtf8("table_tv"))
        self.table_tv.horizontalHeader().setMinimumSectionSize(30)
        self.table_tv.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.table_tv, 0, 0, 1, 1)
        LinksWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(LinksWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LinksWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(LinksWindow)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        LinksWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(LinksWindow)
        self.toolBar_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        LinksWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionAdd = QtGui.QAction(LinksWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/sitemap_color.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd.setIcon(icon)
        self.actionAdd.setObjectName(_fromUtf8("actionAdd"))
        self.actionRemove = QtGui.QAction(LinksWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove.setIcon(icon1)
        self.actionRemove.setObjectName(_fromUtf8("actionRemove"))
        self.actionClear = QtGui.QAction(LinksWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/recycle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon2)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionExport = QtGui.QAction(LinksWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/table_export.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport.setIcon(icon3)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionPrefs = QtGui.QAction(LinksWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/setting_tools.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrefs.setIcon(icon4)
        self.actionPrefs.setObjectName(_fromUtf8("actionPrefs"))
        self.actionAbout = QtGui.QAction(LinksWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/aaaa32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon5)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionBuy = QtGui.QAction(LinksWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/point_gold.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBuy.setIcon(icon6)
        self.actionBuy.setObjectName(_fromUtf8("actionBuy"))
        self.actionSyno = QtGui.QAction(LinksWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/emotion_spy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSyno.setIcon(icon7)
        self.actionSyno.setObjectName(_fromUtf8("actionSyno"))
        self.actionUndo = QtGui.QAction(LinksWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon8)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionScript = QtGui.QAction(LinksWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/script.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScript.setIcon(icon9)
        self.actionScript.setObjectName(_fromUtf8("actionScript"))
        self.toolBar.addAction(self.actionAdd)
        self.toolBar.addAction(self.actionSyno)
        self.toolBar.addAction(self.actionExport)
        self.toolBar.addAction(self.actionClear)
        self.toolBar_2.addAction(self.actionPrefs)
        self.toolBar_2.addAction(self.actionBuy)
        self.toolBar_2.addAction(self.actionAbout)

        self.retranslateUi(LinksWindow)
        QtCore.QMetaObject.connectSlotsByName(LinksWindow)

    def retranslateUi(self, LinksWindow):
        LinksWindow.setWindowTitle(_translate("LinksWindow", "ZSiteMap", None))
        self.toolBar.setWindowTitle(_translate("LinksWindow", "Инструменты", None))
        self.toolBar_2.setWindowTitle(_translate("LinksWindow", "Настройки", None))
        self.actionAdd.setText(_translate("LinksWindow", "Добавить", None))
        self.actionAdd.setToolTip(_translate("LinksWindow", "Добавить", None))
        self.actionRemove.setText(_translate("LinksWindow", "Удалить", None))
        self.actionRemove.setToolTip(_translate("LinksWindow", "Удалить", None))
        self.actionClear.setText(_translate("LinksWindow", "Очистить", None))
        self.actionExport.setText(_translate("LinksWindow", "Экспорт", None))
        self.actionPrefs.setText(_translate("LinksWindow", "Настройки", None))
        self.actionPrefs.setToolTip(_translate("LinksWindow", "Настройки", None))
        self.actionAbout.setText(_translate("LinksWindow", "О программе", None))
        self.actionBuy.setText(_translate("LinksWindow", "Купить", None))
        self.actionSyno.setText(_translate("LinksWindow", "Синонимы", None))
        self.actionUndo.setText(_translate("LinksWindow", "Отмена", None))
        self.actionScript.setText(_translate("LinksWindow", "Скрипт", None))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LinksWindow = QtGui.QMainWindow()
    ui = Ui_LinksWindow()
    ui.setupUi(LinksWindow)
    LinksWindow.show()
    sys.exit(app.exec_())

