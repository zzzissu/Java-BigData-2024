# file : p48_transApp.py
# desc : PyQt5 구글번역 앱

# > pip install googletrans
# 모듈, 라이브러리 설치시 버전 업/다운
# > pip install googletrans==3.1.0a0
# > pip install googletrans==4.0.0rc1

import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from googletrans import Translator

class qtApp(QWidget):
    def __init__(self) -> None: 
        super().__init__()
        self.initUI()
        self.myTrans = Translator() # 구글번역기 객체생성
       
    def initUI(self):   # ui파일을 로드해서 화면 디자인 사용
        uic.loadUi('./day07/transApp.ui', self)
        
        self.setWindowTitle('구글 번역앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리
        self.btnTrans.clicked.connect(self.btnTransClicked) # ui파일 내 위젯은 자동완성 안됨
        self.txtBaseText.returnPressed.connect(self.btnTransClicked)

        self.show()
        
    def btnTransClicked(self):
    #    QMessageBox.about(self,'번역', '번역시작')
        text = self.txtBaseText.text().strip()
        if len(text) != 0:
            result = self.myTrans.translate(text, src='auto', dest='en')
            self.txbResult.append(result.text)
               
    def closeEvent(self, QCloseEvent) -> None:  # 우리식으로 오버라이드(재정의)
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes:   # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()    # 돌아가기(취소)

app = QApplication(sys.argv)
inst = qtApp()
app.exec_()