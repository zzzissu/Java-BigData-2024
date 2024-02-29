# file : p45_notthreadApp.py
# desc : PyQt5 스레드 학습용(스레드 사용안함)



import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtApp(QWidget):
    def __init__(self) -> None: 
        super().__init__()
        self.initUI()
       
    def initUI(self):   # ui파일을 로드해서 화면 디자인 사용
        uic.loadUi('./day07/testThread.ui', self)
        
        self.setWindowTitle('노쓰레드앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui파일 내 위젯은 자동완성 안됨

        self.show()
        
    def btnStartClicked(self):
        self.pgbTask.setValue(0)    # 재설정
        self.pgbTask.setRange(0, 99)    # 프로그래스바 범위설정
        self.btnStart.setDisabled(True)
        # UI(메인)스레드가 화면을 그릴 수 있는 여유가 없음(응답없음 발생)
        for i in range(0, 100):     #0~99
            print(f'노쓰레드 진행 >> {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'노쓰레드 진행 >> {i}')
        self.btnStart.setEnabled(True)
               
    def closeEvent(self, QCloseEvent) -> None:  # 우리식으로 오버라이드(재정의)
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes:   # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()    # 돌아가기(취소)

app = QApplication(sys.argv)
inst = qtApp()
app.exec_()
