#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = 'helljump'

from cx_Freeze import setup, Executable
from time import gmtime, strftime


base = 'Win32GUI'
ver = strftime("%y.%m.%d.%H%M", gmtime())


setup(
    name='ZSiteMap',
    description='Zipta Sitemap by helljump',
    version=ver,
    options={'build_exe': {
        'includes': ['lxml._elementpath', 'gzip', 'jinja2.ext', 'grab.transport.curl'],
        'excludes': ['userdata'],
        'optimize': 9,
        'silent': True,
        'copy_dependent_files': True,
        'include_files': [
            (r'c:\Python27\Lib\site-packages\PyQt4\translations\qt_ru.qm', 'qt_ru.qm'),
            'tcejdbdll.dll',
            'syno.tcn',
        ],
    }},
    executables=[Executable('links.py', base=base, icon="res/aaaa32.ico", targetName="main.exe")]
)
