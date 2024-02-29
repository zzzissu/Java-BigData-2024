# file : p47_qrCodeApp.py
# desc : PyQt5 QR코드 앱

# pip install qrcode
import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qrcode

class qtApp(QWidget):
    def __init__(self) -> None: 
        super().__init__()
        self.initUI()
       
    def initUI(self):   # ui파일을 로드해서 화면 디자인 사용
        uic.loadUi('./day07/qrApp.ui', self)
        
        self.setWindowTitle('QR코드 생성기')
        self.setWindowIcon(QIcon('./images/QR.png'))
        # 버튼 시그널처리
        self.btnGenerate.clicked.connect(self.btnGenerateClicked) # ui파일 내 위젯은 자동완성 안됨

        self.show()
        
    def btnGenerateClicked(self):
       data = self.txtQrData.text()

       if len(data.strip()) == 0:
           QMessageBox.about(self, '경고', '데이터를 입력하세요.')
           return
       else:
           imgPath = './day07/qr.png'
           qrImage = qrcode.make(data)
           qrImage.save('./day07/qr.png')
           img = QPixmap(imgPath)
           self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(300))
       
               
    def closeEvent(self, QCloseEvent) -> None:  # 우리식으로 오버라이드(재정의)
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes:   # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()    # 돌아가기(취소)

app = QApplication(sys.argv)
inst = qtApp()
app.exec_()