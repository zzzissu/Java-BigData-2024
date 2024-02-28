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
import webbrowser   # 기본 웹브라우저 모듈
from naverSearch import NaverSearch
import datetime
import time

class qtApp(QWidget):
    def __init__(self) -> None: 
        super().__init__()
        self.initUI()
       
    def initUI(self):   # ui파일을 로드해서 화면 디자인 사용
        uic.loadUi('./day06/naverNews.ui', self)
        
        self.setWindowIcon(QIcon('./images/news.png'))
        # 버튼 시그널처리
        self.btnSearch.clicked.connect(self.btnSearchClicked) # ui파일 내 위젯은 자동완성 안됨
        self.txtSearchWord.returnPressed.connect(self.btnSearchClicked)     # 검색버튼 시그널 함수를 연결(엔터 누르면 검색작동)
        self.tblSearchResult.itemSelectionChanged.connect(self.tblResultSelected)

        self.show()
        
    def tblResultSelected(self):    # 테이블 클릭시 처리
        select = self.tblSearchResult.currentRow()  # 현재 선택된 행위 인덱스
        url = self.tblSearchResult.item(select, 1).text()
        # QMessageBox.about(self, 'popup', url)
        webbrowser.open(url)        # 웹브라우저 연동

        
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
        # print(jsonSearch)
        self.makeTable(jsonSearch)   # 검색결과로 리스트뷰를 만드는 함수 호출
        
    def makeTable(self, data):
        result = data['items']  # 네이버검색 결과의 키 items의 값들만 활용
        # lsvSearchResult 리스트뷰 작업시작
        self.tblSearchResult.setColumnCount(3)
        self.tblSearchResult.setRowCount(len(result))   # 10개면 10개
        self.tblSearchResult.setHorizontalHeaderLabels(['기사제목', '뉴스링크', '개시일자'])
        
        n = 0
        for post in result:
            self.tblSearchResult.setItem(n, 0, QTableWidgetItem(post['title']))
            self.tblSearchResult.setItem(n, 1, QTableWidgetItem(post['link']))
            tempDates = str(post['pubDate']).split(' ')
            year = tempDates[3]
            month = time.strptime(tempDates[2], '%b').tm_mon
            month = f'{month:02d}'
            day = tempDates[1]
            date = f'{year}-{month}-{day}'
            self.tblSearchResult.setItem(n, 2, QTableWidgetItem())
            n += 1
            
        self.tblSearchResult.setColumnWidth(0, 465)     # 내용의 칸 크기 조정
        self.tblSearchResult.setColumnWidth(1, 200)
        self.tblSearchResult.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 컬럼 더블클릭(수정) 금지

       
    def closeEvent(self, QCloseEvent) -> None:  # 우리식으로 오버라이드(재정의)
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes:   # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()    # 돌아가기(취소)

app = QApplication(sys.argv)
inst = qtApp()
app.exec_()
