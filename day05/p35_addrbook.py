# file : p35_addrbook.py
# desc : 콘솔 주소록 프로그램

import os

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
        
    def __str__(self) -> str:   # 원래 출력 <__main__.Contact object at 0x0000024500772150>
        res = (f'이  름: {self.__name}\n'
               f'핸드폰: {self.__phoneNumber}\n'
               f'이메일: {self.__eMail}\n'
               f'주  소: {self.__addr}')
        return res
    
def setContact():   # 사용자 입력으로 주소록 받기 함수
    (name, phoneNumber, eMail, addr) = input('입력(이름, 핸드폰, 이메일, 주소[/]) > ').split('/')
    name = name.strip()         # strip = 사용자로 인한 앞, 뒤 스페이스 공백을 제거
    phoneNumber = phoneNumber.strip()
    eMail = eMail.strip()
    addr = addr.strip()
    # print(f'"{name}", "{phoneNumber}", "{eMail}", "{addr}"')
    contact = Contact(name, phoneNumber, eMail, addr)   # 매개변수 명과 동일하게 로컬변수 이름 지정
    return contact
    
def displayManu():
    menu = ('주소록 프로그램 \n'
            '1. 연락처 추가 \n'
            '2. 연락처 출력 \n'
            '3. 연락처 삭제 \n'
            '4. 종료')
    print(menu)
    sel = int(input('메뉴입력 : '))
    return sel

def clearConsole():
    cmd = 'clear'   #mac OD, Linux, Unix 명령어
    if os.name in ('nt', 'dos'):    #window
        cmd = 'cls' #window 명령어
        
    os.system(cmd)  # 명령어 실행
    
def getContacts(list):  # 리스트를 받아서 출력함수
    for item in list:
        print(item)
    
def run():
    # 연락처를 담을 주소록 리스트 생성
    listContact = []
    
    clearConsole()  # 화면을 클리어
    while True:
        selMenu = displayManu()
        if selMenu == 1:    # 연락처 추가인 경우
            clearConsole()
            contact = setContact()
            listContact.append(contact)
            # print(listContact)
            input() # 엔터를 입력하도록 유도
            clearConsole()
        elif selMenu == 2:  # 연락처 출력
            clearConsole()
            getContacts(listContact)
            input()
            clearConsole()
        elif selMenu == 4:
            break
        else:
            clearConsole()
    # setContact()
    # first = Contact('홍길동', '010-8532-4832', 'fswe@naver.com', '경성')      # 위의 순서와 맞게 입력
    # first = Contact(addr='경성', phoneNumber='010-8532-4832', name='홍길동', eMail='fswe@naver.com')
    # print(first)
    
if __name__ == '__main__':  # 메인트리
    print('프로그램 시작')
    run()   #메인함수 실행

print('프로그램 종료')
