# file : naverSearch.py
# desc : 네이버 검색용 API 클래스
import datetime
import json
from urllib.request import Request, urlopen
from urllib.parse import quote  # 글자를 유니코드(utf-8 인코딩 함수)
# import ssl

class NaverSearch:
    def __init__(self) -> None:
        print('naver API 클래스 생성')

    # URL로 검색시작 함수
    def getRequestUrl(self, url):   # 클래스 내에서 사용할 함수
        # ssl._create_default_https_context = ssl._create_unverified_context
        req = Request(url)
        req.add_header('X-Naver-Client-Id', 'VYHLpNOKpGsK9SLKbgOy') # 자신의 애플리케이션 클라이언트 아이디 입력
        req.add_header('X-Naver-Client-Secret', 'VQlLzjfIAD')   # 시크릿키는 숨겨져있기 때문에 (보기)클릭
        
        try:
            res = urlopen(req)
            if res.status == 200:
                print(f'[{datetime.datetime.now()}]: URL 요청 성공')
                return res.read().decode('utf-8')
        except Exception as e:
            print(f'[{datetime.datetime.now()}]: URL 요청 오류! {e.args}')
            return None # 예외가 발생하면 아무 값도 돌려주지 않음(None 값을 넘김)
        
    # 실제 동작함수 생성
    
    def getSearchResult(self, searchWord):
        baseUrl = 'https://openapi.naver.com/v1/search/news.json'
        params = f'?query={quote(searchWord)}&start=1&display=100'
        finalUrl = baseUrl + params
        
        result = self.getRequestUrl(finalUrl)
        if result != None:  # 예외가 발생하지 않으면
            return json.loads(result)
        else:
            return None