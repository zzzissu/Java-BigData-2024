# file : p31_externalLib.py
# desc :  외부 라이브러리 사용법

# > pip install LibName
# Successfully installed / Requirement already satisfied 가 나와야 함
# > pop uninstall LibName
# Successfully uninstalled 나와야 함

from faker import Faker

dummy = Faker('ko-KR')  # 한국어 설정
print(dummy.items().pop())

fake = Faker('ko-KR')
print(fake.name())
print(fake.address())
# print(fake.profile())

dummyData = [(fake.profile()) for _ in range(10)]
print(dummyData)

## urllib3 외부 웹페이지 분석 모듈
import requests
from bs4 import BeautifulSoup

# res = requests.get('https://www.naver.com')
# print(res.status_code)
# print(res.content)  # 내용가져오기

res = requests.get('https://www.naver.com')

if res.status_code == 200:
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    