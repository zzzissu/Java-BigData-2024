# file : p40_naverNewsApp.py
# desc : PyQt5, PyQt5Designer naver API 연동 뉴스 검색 앱 만들기
'''
설치 > pip install PyQt5
설치 > pip install PyQt5Designer
'''

import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from naverSearch import NaverSearch

class qtApp(QWidget):
    def __init__(self) -> None: 
        super().__init__()
        self.initUI()
       
    def initUI(self):   # ui파일을 로드해서 화면 디자인 사용
        uic.loadUi('./day06/naverNews.ui', self)
        
        self.setWindowIcon(QIcon('./images/news.png'))
        # 버튼 시그널처리
        self.btnSearch.clicked.connect(self.btnSearchClicked) # ui파일 내 위젯은 자동완성 안됨

        self.show()
        
    def btnSearchClicked(self):
        searchWord = self.txtSearchWord.text().strip()   # strip을 넣어주면 공백에 검색 작동하지 않음(검색어를 입력하세요 출력)
        
        
        if (len(searchWord)) == 0:  # validation Check(입력 검증)
            QMessageBox.about(self, '네이버검색', '검색어를 입력하세요')
            return  # 함수 탈출
        
        # QMessageBox.about(self, '네이버 검색', '검색 시작')
        # self.label.setText('What the F*!')  # 클릭박스를 누르면 창 내용이 바뀜
        
        # 검색 시작
        api = NaverSearch() # api 객체 생성
        jsonSearch = api.getSearchResult(searchWord)
        print(jsonSearch)

       
    def closeEvent(self, QCloseEvent) -> None:  # 우리식으로 오버라이드(재정의)
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes:   # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()    # 돌아가기(취소)

app = QApplication(sys.argv)
inst = qtApp()
app.exec_()
