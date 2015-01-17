!define PROGNAME "Zipta Sitemap"
!include "MUI2.nsh"
!include "FileFunc.nsh"
!define MUI_WELCOMEPAGE_TITLE_3LINES
!define PROGPATH "\${PROGNAME}"
!define PROGEXE "main.exe"

OutFile "c:\Users\snoa\YandexDisk\софт\zipta-sitemap-dist.exe"
Name "${PROGNAME}"
WindowIcon on
Icon "res\aaaa32.ico"
XPStyle on
SetCompressor /SOLID lzma
InstallDir "$PROGRAMFILES${PROGPATH}"
RequestExecutionLevel admin

!define MUI_ABORTWARNING
!define MUI_WELCOMEPAGE_TITLE "Добро пожаловать в установщик ${PROGNAME}"
!define MUI_WELCOMEPAGE_TEXT "По всем вопросам обращайтесь на наш сайт zipta.ru либо по icq 125521555"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "res\license.txt"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_LANGUAGE "Russian"

Section ""
    SetOutPath $INSTDIR
    File /r /x *.pyc /x *.pye /x *.py build\exe.win32-2.7\*.*
    CreateShortCut "$Desktop\${PROGNAME}.lnk" "$INSTDIR\${PROGEXE}" "" "$INSTDIR\${PROGEXE}" 0
SectionEnd
