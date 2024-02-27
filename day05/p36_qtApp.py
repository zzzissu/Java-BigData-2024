# file ; p36_qtApp.py
# desc : PyQt5 앱 만들기
'''
PyQt5 -> Qt를 파이썬에서 쓸 수 있도록 만든 라이브러리
Qt -> C, C++ 사용할 GUI(Graphical User Interface WinApp) 프레임워크(멀티플랫폼)

설치 > pip install PyQt5
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
# QApplication 만들 앱의 전체를 관리하는 클래스
# QWidget 메뉴가 없는 윈도우 앱
# QMainWindow 메뉴가 있는 윈도우 앱
from PyQt5.QtWidgets import *

class qtApp(QWidget):   # QWidget이 가지고 있는 속성, 변수, 함수를 모두 사용 가능       # 상속
    def __init__(self) -> None: 
        super().__init__()  # 생성자, 부모클래스의 생성자 함수도 실행되어야 함
        self.initUI();
       
    def initUI(self):
        self.setGeometry(300, 300, 800, 400)
        # (왼쪽 위 모서리가 기준)앞 두 수는 창을 띄울 위치(x축, y축), 뒤 두 수는 창의 크기(x축, y축)
        self.setWindowTitle('첫번째 윈도우앱')
        self.setWindowIcon(QIcon('./images/windows.png'))       # 왼위 모서리 아이콘 수정
        self.show() # 윈도우 창 띄우기
        
    def paintEvent(self, event) -> None:       # paintEvent  = QWidget 클래스에 존재하기 때문에 가져올 수 있음
        paint = QPainter()       # Event : 클릭, 드래그, 타이핑 등 동작의 모든것을 의미
        paint.begin(self)   # 그림을 그리기 시작하면
        paint.setPen(QColor(200, 0, 0))     # R, G, B
        paint.setFont(QFont('Bauhaus 93', 40))     # 글씨체, 글씨크기
        paint.drawText(250, 400//2, 'Hello PyQt!')   
        paint.end() # 반드시 닫아야 함
        
app = QApplication(sys.argv)
inst = qtApp()  # 객체 생성
app.exec_() # exec_ = 함수 실행
