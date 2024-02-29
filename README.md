# 빅데이터 언어 2024

빅데이터 자바 개발자 파이썬 학습 리포지토리

## 1일차

- 파이썬 개발환경

  - [깃 설치](https://git-scm.com/downloads)
  - [깃허브 데스크탑 설치](https://desktop.github.com/)
  - [파이썬 설치](https://www.python.org/)
  - [Visual Studio Code 설치](https://code.visualstudio.com/download)
  - [나눔고딕코딩 글자체 설치](https://github.com/naver/nanumfont)

- 파이썬 학습

  - 파이썬 개요
    - 1990년 네덜란드 개발자 귀도 반 로섬이 개발
    - 쉽고 간결한 문법, 무료, 빠른 개발속도
  - 파이썬 기초문법

    - 숫자형(정수, 실수, 진수)

    ```python
    # 변수만 선언, 값만 할당하면 숫자형으로 지정
    # c, c++, java, c#처럼 형지정이 없음
    val = 10 # 정수형
    val = 2.15 # 실수형
    # 특수 숫자형
    binVal = 0b11111111 # 255
    octVal = 0o11 # 9 # 1~7 10(8)
    hexVal = 0xFF # 255 # 0~9 ABCDEF
    print('2진수', binVal, '8진수', octVal, '16진수', hexVal)
    ```

    - 문자열(특수형태 리스트)형(기본 문자열, 연산, 문자열 포맷, 함수)

    ```python
      # '', "" 모두 사용 가능
    ```

    - 리스트형, 튜플형(연산, 함수)
      - 리스트는 수정, 삭제 가능
      - 튜플은 수정, 삭제 불가 / 그 외는 리스트와 동일

## 2일차

- 파이썬 학습
  - 파이썬 기초문법
    - 딕셔너리, 집합
    - 불형
    - None형
    - 제어문(if, while, for)
    - 제어문 연습
    - 함수

## 3일차

- 파이썬 학습
  - 파이썬 기초문법
    - 입출력
    - 객체지향

## 4일차

- 파이썬 학습
  - 파이썬 기초문법
    - 모듈, 패키지
    - ★★예외처리, 디버깅: 디버깅 예외찾고 거기에 예외처리
    - 내장함수
    - 표준 및 외부 라이브러리

## 5일차

- 파이썬 학습

  - 파이썬 응용

    - OS내 디렉토리 검색
    - 아스키 및 유니코드
    - 주소록 앱 만들기

    ```python
    class Contact:  # 주소록 클래스
        # __name =''
        # __phoneNumber = ''
        # __eMail = ''
        # __addr = ''

        def __init__(self, name, phoneNumber, eMail, addr) -> None:
            self.__name = name
            self.__phoneNumber = phoneNumber
            self.__eMail = eMail
            self.__addr = addr

        # 사용자가 원하는 형태로 출력
        def __str__(self) -> str:   # 원래 출력 <__main__.Contact object at 0x0000024500772150>
            res = (f'이  름: {self.__name}\n'
                  f'핸드폰: {self.__phoneNumber}\n'
                  f'이메일: {self.__eMail}\n'
                  f'주  소: {self.__addr}')
            return res

        # 연락처 여부확인
        def isNameExist(self, name):
            if self.__name == name: # 찾는 이름 존재
                return True
            else:
                return False

        def getInfo(self):
            return self.__name, self.__phoneNumber, self.__eMail, self.__addr
    ```

    ![주소록 앱](https://raw.githubusercontent.com/zzzissu/Java-BigData-2024/main/images/bigdata01.gif)

    - windows App 만들기(PyQt 5)

    ![QtApp](https://raw.githubusercontent.com/zzzissu/Java-BigData-2024/main/images/bigdata02.png)

## 6일차

- 파이썬 학습

  - PyQt5 학습 이어서

    - QWidget 자식 클래스 종류 학습

    ![QLaebl](https://raw.githubusercontent.com/zzzissu/Java-BigData-2024/main/images/bigdata03.png)

    - Naver 뉴스API 검색 앱

    ![naverApp](https://raw.githubusercontent.com/zzzissu/Java-BigData-2024/main/images/bigdata04.png)

## 7일차

- 파이썬 학습
  - PyQt5 계속
    - naver 뉴스API 검색 앱 마무리
  - json 학습
  - PyQt5
    - 스레드 개념, 학습
