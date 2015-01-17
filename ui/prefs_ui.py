# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prefs.ui'
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

class Ui_PrefsDialog(object):
    def setupUi(self, PrefsDialog):
        PrefsDialog.setObjectName(_fromUtf8("PrefsDialog"))
        PrefsDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        PrefsDialog.resize(433, 216)
        self.gridLayout_4 = QtGui.QGridLayout(PrefsDialog)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.buttonBox = QtGui.QDialogButtonBox(PrefsDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.RestoreDefaults|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_4.addWidget(self.buttonBox, 5, 0, 1, 2)
        self.template_te = SingleLinePlainText(PrefsDialog)
        self.template_te.setObjectName(_fromUtf8("template_te"))
        self.gridLayout_4.addWidget(self.template_te, 3, 1, 1, 1)
        self.label = QtGui.QLabel(PrefsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(PrefsDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.threads_sb = QtGui.QSpinBox(PrefsDialog)
        self.threads_sb.setMinimum(1)
        self.threads_sb.setProperty("value", 3)
        self.threads_sb.setObjectName(_fromUtf8("threads_sb"))
        self.gridLayout_4.addWidget(self.threads_sb, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(PrefsDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.maximum_sb = QtGui.QSpinBox(PrefsDialog)
        self.maximum_sb.setMinimum(100)
        self.maximum_sb.setMaximum(10000)
        self.maximum_sb.setSingleStep(10)
        self.maximum_sb.setProperty("value", 2000)
        self.maximum_sb.setObjectName(_fromUtf8("maximum_sb"))
        self.gridLayout_4.addWidget(self.maximum_sb, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(PrefsDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)
        self.pause_sb = QtGui.QSpinBox(PrefsDialog)
        self.pause_sb.setObjectName(_fromUtf8("pause_sb"))
        self.gridLayout_4.addWidget(self.pause_sb, 2, 1, 1, 1)

        self.retranslateUi(PrefsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), PrefsDialog.clickedBB)
        QtCore.QMetaObject.connectSlotsByName(PrefsDialog)

    def retranslateUi(self, PrefsDialog):
        PrefsDialog.setWindowTitle(_translate("PrefsDialog", "Настройки", None))
        self.template_te.setPlainText(_translate("PrefsDialog", "{{ title }}|{{ link }}|{{description}}", None))
        self.label.setText(_translate("PrefsDialog", "Шаблон строки", None))
        self.label_2.setText(_translate("PrefsDialog", "Потоков", None))
        self.label_3.setText(_translate("PrefsDialog", "Ограничение размера\n"
"страницы", None))
        self.maximum_sb.setSuffix(_translate("PrefsDialog", " байт", None))
        self.label_4.setText(_translate("PrefsDialog", "Пауза между\n"
"запросами", None))
        self.pause_sb.setSuffix(_translate("PrefsDialog", " секунд", None))

from singlelineplaintext import SingleLinePlainText
import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PrefsDialog = QtGui.QDialog()
    ui = Ui_PrefsDialog()
    ui.setupUi(PrefsDialog)
    PrefsDialog.show()
    sys.exit(app.exec_())

