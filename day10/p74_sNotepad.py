# file : p74_sNotepad.py
# desc : 메모장 만들기

import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent, QMouseEvent
from PyQt5.QtWidgets import *
# 리소스 파일 추가

class WinApp(QMainWindow):   # QWidget이 아님!
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()
        
    def initUI(self):
        uic.loadUi('./day10/snote.ui', self)
        # self.setWindowIcon(QIcon('./day09/imgs/editor.png'))
        self.show()
        
    def initSignal (self):
        # 메뉴/툴바 액션에 대한 시그널처리함수 선언...
        self.action_Open.triggered.connect(self.action0penClicked)
        self.action_Save.triggered.connect(self.actionSaveClicked)
        self.action_Save_as.triggered.connect(self.actionSaveAsClicked)
        self.action_Quit.triggered.connect(self.actionQuitClicked)
        self.action_About.triggered.connect(self.actionAboutClicked)

    def action0penClicked(self):
        QMessageBox.about(self, '메모장', 'new')
        
    def actionSaveClicked(self):
        QMessageBox.about(self, '메모장', 'save')

    def actionSaveAsClicked(self):
        QMessageBox.about(self, '메모장', 'open')
        
    def actionAboutClicked(self):
        QMessageBox.about(self, '메모장', 'about')
        
    def actionQuitClicked(self):
        exit(0)
        
    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: QCloseEvent.accept()
        else:QCloseEvent.ignore()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())