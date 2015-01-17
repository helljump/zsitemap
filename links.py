#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = 'helljump'

import logging
log = logging.getLogger(__name__)


from PyQt4 import QtCore
from PyQt4 import QtGui
import transaction
import startup
from persistent.list import PersistentList
from ui.links_ui import Ui_LinksWindow
from helpers import Link, MyProgressDialog
from about import AboutDialog
from prefs import PrefsDialog, TEMPLATE
from query import QueryDialog
import Queue
from grab import Grab
import re
import threading
from jinja2 import Environment
import codecs
from syno import Syno, SynoDialog
import types


class Message():

    MAP, PAGE, ADD, DONE = range(4)

    def __init__(self, cmd, param):
        self.cmd = cmd
        self.param = param


DBLOCK = threading.Lock()


class Worker(QtCore.QThread):

    process = QtCore.pyqtSignal(object)

    def __init__(self, queue, parent):
        super(Worker, self).__init__(parent)
        self.queue = queue
        self.active = True
        self.g = Grab()
        self.g.setup(hammer_mode=True)
        self.maximum = startup.CFG.value('prefs/maximum', 2000, type=int)
        self.pause = startup.CFG.value('prefs/pause', 0, type=int)

    def run(self):
        log.debug("start %s" % QtCore.QThread.currentThread())
        conn = startup.DB.open()
        root = conn.root()
        items = root["links"]
        while self.active:
            try:
                message = self.queue.get_nowait()
                if message.cmd == Message.MAP:
                    rc = self.g.go(message.param)
                    for row in re.findall('<loc>([^>]+)</loc>', rc.unicode_body()):
                        self.queue.put(Message(Message.PAGE, row))
                        self.process.emit(Message(Message.ADD, u'Обработка %s' % row))
                        if not self.active:
                            break
                    self.process.emit(Message(Message.DONE, u'Получена карта %s' % message.param))
                elif message.cmd == Message.PAGE:
                    self.g.go(message.param, body_maxsize=self.maximum)
                    if not self.active:
                        break
                    doc = self.g.doc
                    t = doc.select('//title')
                    title = t.text() if t else u'Нет заголовка'
                    t = doc.select('//meta[@name="description"]/@content')
                    description = t.text() if t else u'Нет описания'
                    with DBLOCK:
                        transaction.begin()
                        l = Link(message.param, title, description)
                        if l not in items:
                            items.append(l)
                        transaction.commit()
                    self.process.emit(Message(Message.DONE, u'Добавили ссылку %s' % message.param))
            except Queue.Empty:
                QtCore.QThread.usleep(10)
            except:
                transaction.abort()
                self.process.emit(Message(Message.DONE, u'Ошибка, смотри логи.'))
                log.exception('worker error')
            QtCore.QThread.sleep(self.pause)
        conn.close()
        log.debug("stop %s" % QtCore.QThread.currentThread())


class LinksModel(QtCore.QAbstractTableModel):

    def __init__(self, parent):
        super(LinksModel, self).__init__(parent)
        self.labels = [u'Ссылка', u'Заголовок', u'Описание']
        root = startup.CONN.root()
        if "links" not in root:
            root["links"] = PersistentList()
            transaction.commit()
        self._data = root["links"]

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.labels)

    def headerData(self, section, orientation, role):
        egg = QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            egg = QtCore.QVariant(self.labels[section])
        elif orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            egg = QtCore.QVariant(section + 1)
        return egg

    def flags(self, index):
        egg = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        return egg

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None
        item = self._data[index.row()]
        ndx = index.column()
        egg = QtCore.QVariant()
        if role == QtCore.Qt.DisplayRole:
            if ndx == 0:
                egg = item.url
            elif ndx == 1:
                egg = item.title
            elif ndx == 2:
                egg = item.description
        return egg

    def removeRows(self, row, count, parent=QtCore.QModelIndex()):
        if row < 0 or row > len(self._data):
            return False
        self.beginRemoveRows(parent, row, row+count-1)
        while count != 0:
            del self._data[row]
            count -= 1
        self.endRemoveRows()
        return True

    def add_item(self, item):
        r = len(self._data)
        if item in self._data:
            return
        self.beginInsertRows(QtCore.QModelIndex(), r, r)
        self._data.append(item)
        self.endInsertRows()
        return self.createIndex(r, 1)

    def clear(self, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(parent, 0, self.rowCount()-1)
        del self._data[:]
        self.endRemoveRows()


class LinksWindow(QtGui.QMainWindow, Ui_LinksWindow):

    def __init__(self, parent=None):
        super(LinksWindow, self).__init__(parent)
        self.setupUi(self)
        if startup.CFG.contains("links/state"):
            self.restoreState(startup.CFG.value("links/state").toByteArray())
        if startup.CFG.contains("links/geometry"):
            self.restoreGeometry(startup.CFG.value("links/geometry").toByteArray())
        self.progress = QtGui.QProgressBar(self)
        self.statusbar.addPermanentWidget(self.progress)

        self.model = LinksModel(self)
        self.table_tv.setModel(self.model)
        self.table_tv.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        #self.table_tv.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.table_tv.addAction(self.actionRemove)
        self.actionBuy.setVisible(False)
        '''
        try:
            u = __import__('userdata')
            self.export = types.MethodType(u.export, self)
        except ImportError:
            log.exception('import error')
        '''
            
    def closeEvent(self, event):
        self.table_tv.setModel(None)
        startup.CFG.setValue('links/state', self.saveState())
        startup.CFG.setValue('links/geometry', self.saveGeometry())
        event.accept()

    @QtCore.pyqtSlot()
    def on_actionAbout_triggered(self):
        AboutDialog(self).exec_()

    @QtCore.pyqtSlot()
    def on_actionPrefs_triggered(self):
        PrefsDialog(self).exec_()

    @QtCore.pyqtSlot()
    def on_actionExport_triggered(self):
        log.debug('export')
        self.export()

    def export(self):
        fname = QtGui.QFileDialog.getSaveFileName(self, u'Экспорт', filter=u'Текстовый файл (*.txt)')
        if not fname:
            return
        fname = unicode(fname)
        env = Environment()
        s = startup.CFG.value('prefs/template', TEMPLATE, unicode)
        template = env.from_string(unicode(s))
        try:
            self.toolBar.setDisabled(True)
            links = startup.CONN.root()['links']
            self.progress.setRange(0, len(links))
            fout = codecs.open(fname, 'w', 'utf8')
            for i, link in enumerate(links):
                data = template.render({'title': link.title, 'link': link.url,
                    'description': link.description})
                fout.write(data)
                fout.write('\n')
                self.progress.setValue(i)
            fout.close()
            self.statusBar().showMessage(u'Готово', 3000)
        except IOError:
            QtGui.QMessageBox.critical(self, u"Экспорт", u"Ошибка записи в файл.")
        finally:
            self.progress.reset()
            self.toolBar.setEnabled(True)

    @QtCore.pyqtSlot()
    def on_actionSyno_triggered(self):
        log.debug('syno')
        dlg = SynoDialog(self)
        rc = dlg.exec_()
        if not rc:
            return
        intitle = dlg.title_cb.checkState() == QtCore.Qt.Checked
        indesc = dlg.description_cb.checkState() == QtCore.Qt.Checked
        links = startup.CONN.root()['links']
        s = Syno()
        self.progress.setRange(0, len(links))
        try:
            self.toolBar.setDisabled(True)
            transaction.begin()
            for i, link in enumerate(links):
                self.progress.setValue(i)
                if intitle:
                    link.title = s(link.title)
                if indesc:
                    link.description = s(link.description)
            transaction.commit()
            self.refresh()
            self.statusBar().showMessage(u'Готово', 3000)
        except:
            log.exception('syno error')
            transaction.abort()
        finally:
            self.progress.reset()
            self.toolBar.setEnabled(True)

    @QtCore.pyqtSlot()
    def on_actionAdd_triggered(self):
        log.debug('add')
        dlg = QueryDialog(self)
        rc = dlg.exec_()
        if not rc:
            return
        links = dlg.get_links()
        workers = []
        thc = startup.CFG.value("prefs/threads", 3, int)
        counter = {'current': 0, 'total': 0}
        queue = Queue.Queue()
        for l in links:
            queue.put(Message(Message.MAP, l))
            counter['total'] += 1
        pdlg = MyProgressDialog(u'Обработка', u'Подключение', u'Отмена', parent=self)

        def closed():
            log.debug('closed')
            for w in workers:
                w.process.disconnect()
                w.active = False
            transaction.commit()
            self.refresh()

        def process(t):
            pdlg.set_text(t.param)
            if t.cmd == Message.ADD:
                counter['total'] += 1
                pdlg.setMaximum(counter['total'])
            elif t.cmd == Message.DONE:
                counter['current'] += 1
                pdlg.setValue(counter['current'])
                if counter['total'] <= counter['current']:
                    pdlg.close()

        pdlg.closed.connect(closed)

        for i in range(thc):
            w = Worker(queue, self)
            w.process.connect(process)
            workers.append(w)
            w.start()

        pdlg.show()

    def refresh(self):
        model = self.table_tv.model()
        from_ = model.index(0, 0)
        to_ = model.index(len(model._data)-1, len(model.labels)-1)
        model.dataChanged.emit(from_, to_)
        model.layoutChanged.emit()

    @QtCore.pyqtSlot()
    def on_actionClear_triggered(self):
        log.debug('clear all')
        rc = QtGui.QMessageBox.question(self, u'Удалить', u'Удалить все?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if rc != QtGui.QMessageBox.Yes:
            return
        self.table_tv.model().clear()
        transaction.commit()
        self.statusBar().showMessage(u'Очистили', 3000)

    @QtCore.pyqtSlot()
    def on_actionRemove_triggered(self):
        rows = [ndx for ndx in self.table_tv.selectedIndexes() if ndx.column() == 1]
        rc = QtGui.QMessageBox.question(self, u'Удаление', u'Удалить выбранные?',
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if rc == QtGui.QMessageBox.No:
            return
        rows.sort(key=QtCore.QModelIndex.row, reverse=True)
        for ndx in rows:
            self.model.removeRow(ndx.row())
        transaction.commit()
        self.statusBar().showMessage(u'Удалили', 3000)

    @QtCore.pyqtSlot()
    def on_actionBuy_triggered(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('http://zipta.ru'))


if __name__ == '__main__':

    dlg = LinksWindow()
    startup.SPLASH.finish(dlg)
    dlg.show()
    QtGui.qApp.exec_()


