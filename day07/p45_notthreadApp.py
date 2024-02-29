# file : p45_notthreadApp.py
# desc : PyQt5 스레드 학습용(스레드 사용안함)



import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackgroundWorker(QThread):    # PyQt용 스레드
    initUiSignal = pyqtSignal(int)  # 스레드 진행시 UI에서 초기화부분 시그널 전달
    setPgbSignal = pyqtSignal(int)  # 스레드 진행시 변경되는 숫자를 UI로 전달
    setTxbSignal = pyqtSignal(str)  # 스레드 진행시 화면에 출력될 문자열 UI쪽으로 전달
    
    
    def __init__(self, parent) -> None: # 부모는 qtApp 클래스
        super().__init__(parent)
        self.parent = parent    # 나의 부모가 누구인지 알려줌
        
    def run(self) -> None:
        maxVal = 100
        self.initUiSignal.emit(maxVal)   # 스스로 값을 보내지 못하기 때문에 UI쪽(qtApp)에서 받아서 처리

        for i in range(maxVal):
            print(f'쓰레드 진행 >> {i}')
            self.setPgbSignal.emit(i)
            self.setTxbSignal.emit(f'쓰레드 진행 >> {i}')
            # self.parent.pgbTask.setValue(i) # UI 스레드의 권한을 백그라운드 스레드에 주지 않음
            # self.parent.txbLog.append(f'노쓰레드 진행 >> {i}')  # 사용불가

class qtApp(QWidget):
    def __init__(self) -> None: 
        super().__init__()
        self.initUI()
       
    def initUI(self):   # ui파일을 로드해서 화면 디자인 사용
        uic.loadUi('./day07/testThread.ui', self)
        
        self.setWindowTitle('쓰레드앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui파일 내 위젯은 자동완성 안됨

        self.show()
        
    def btnStartClicked(self):
        self.btnStart.setDisabled(True)
        th = BackgroundWorker(self) # 
        th.start()  # 스레드 내의 run()함수 실행
        th.initUiSignal.connect(self.initPgbTask)
        th.setPgbSignal.connect(self.setPgbTask)
        th.setTxbSignal.connect(self.setTxbLog)
        
        self.btnStart.setEnabled(True)
        
    @pyqtSlot(str)
    def setTxbLog(self, msg):
        self.txbLog.append(msg)
        
    @pyqtSlot(int)
    def setPgbTask(self, val):
        self.pgbTask.setValue(val)

        
    @pyqtSlot(int)  # pyqtSignal에서 넘어온 값을 처리해주는 부분이라고 선언
    def initPgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxVal-1)
        
    def closeEvent(self, QCloseEvent) -> None:  # 우리식으로 오버라이드(재정의)
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes:   # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()    # 돌아가기(취소)

app = QApplication(sys.argv)
inst = qtApp()
app.exec_()
