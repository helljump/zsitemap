#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = 'helljump'

import logging
import startup
import transaction
import PyV8
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import Qsci


log = logging.getLogger(__name__)


def configure_sci(sci):
    font = QtGui.QFont()
    font.setFamily('Courier')
    font.setFixedPitch(True)
    font.setPointSize(10)
    sci.setFont(font)
    sci.setMarginsFont(font)
    fontmetrics = QtGui.QFontMetrics(font)
    sci.setMarginsFont(font)
    sci.setMarginWidth(1, fontmetrics.width("000") + 6)
    sci.setMarginLineNumbers(1, True)
    sci.setMarginsBackgroundColor(QtGui.QColor("#cccccc"))
    sci.setBraceMatching(Qsci.QsciScintilla.SloppyBraceMatch)
    sci.setCaretLineVisible(True)
    sci.setCaretLineBackgroundColor(QtGui.QColor("#e4ffe4"))
    lexer = Qsci.QsciLexerJavaScript()
    lexer.setDefaultFont(font)
    sci.setLexer(lexer)
    sci.SendScintilla(Qsci.QsciScintilla.SCI_STYLESETFONT, 1, 'Courier')
    sci.SendScintilla(Qsci.QsciScintilla.SCI_SETHSCROLLBAR, 0)


class JLink(object):

    def __init__(self, link):
        self.link = link

    @property
    def title(self):
        return self.link.title

    @title.setter
    def title(self, v):
        self.link.title = unicode(v, 'utf8')

    @property
    def url(self):
        return self.link.url

    @url.setter
    def url(self, v):
        self.link.url = unicode(v, 'utf8')

    @property
    def description(self):
        return self.link.description

    @description.setter
    def description(self, v):
        self.link.description = unicode(v, 'utf8')


class JLinks(PyV8.JSClass):

    def __init__(self, links):
        self.links = links

    def __len__(self):
        return len(self.links)

    @property
    def length(self):
        return len(self.links)

    def __getitem__(self, ndx):
        return JLink(self.links[ndx])


def main():
    root = startup.CONN.root()
    links = root['links']

    with PyV8.JSContext() as ctx:
        with PyV8.JSEngine() as engine:
            ctx.enter()
            log.debug('compile')
            s = engine.compile(u'''
                for(i=0; i<links.length; i++){
                    link = links[i]
                    link.title = link.title.replace('е','^');
                    log.debug(link.url);
                }
            ''')
            ctx.locals.log = log
            log.debug('jsarr')
            ctx.locals.links = JLinks(links)
            log.debug('run')
            s.run()
            ctx.leave()
            transaction.commit()

if __name__ == '__main__':
    main()
