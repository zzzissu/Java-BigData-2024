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
    
def setContact():   # 사용자 입력으로 주소록 받기 함수
    (name, phoneNumber, eMail, addr) = input('입력(이름, 핸드폰, 이메일, 주소[/]) > ').split('/')
    name = name.strip()         # strip = 사용자로 인한 앞, 뒤 스페이스 공백을 제거
    phoneNumber = phoneNumber.strip()
    eMail = eMail.strip()
    addr = addr.strip()
    # print(f'"{name}", "{phoneNumber}", "{eMail}", "{addr}"')
    contact = Contact(name, phoneNumber, eMail, addr)   # 매개변수 명과 동일하게 로컬변수 이름 지정
    return contact

def delContact(list, name): # 연락처 삭제 함수
    for i in range(len(list),-1, -1, -1):
        item = list[i]
        if item.isNameExist(name):
            del list[i]
    
    for i, item in enumerate(list):
        if item.isNameExist(name):
            # list.remove(name)
            del list[i]
            
def saveContact(list):  # 연락처 저장함수
  with open('./contacts.txt', mode='w', encoding='utf-8') as fp:
    for item in list:
        name, phoneNumber, eMail, addr = item.getInfo()
        fp.write(f'{name}/{phoneNumber}/{eMail}/{addr}\n')
    
def loadContact(list):  # 처음 실행 시 데이터 읽어오는 함수
    try:
        with open('./contacts.txt', mode='r', encoding='utf-8') as fp:
            while True:
                line = fp.readline()
                if not line: break
                
                lines = line.replace('\n', '').split('/')         # 세이브
                contact = Contact(name=lines[0], phoneNumber=lines[1], eMail=lines[2], addr=lines[3])
                list.append(contact)
    except: # 연락처 파일이 없으면 새로 만들어줌
        f = open('./contacts.txt', mode='w', encoding='utf-8')
        f.close()
        
def displayManu():
    menu = ('주소록 프로그램 \n'
            '1. 연락처 추가 \n'
            '2. 연락처 출력 \n'
            '3. 연락처 삭제 \n'
            '4. 종료')
    print(menu)
    try:
        sel = int(input('메뉴입력: '))
    except:     # 1~4가 아닌 잘못된 문자를 입력할 때 예외처리
        sel = 0
    return sel

def clearConsole():
    cmd = 'clear'   #mac OD, Linux, Unix 명령어
    if os.name in ('nt', 'dos'):    #window
        cmd = 'cls' #window 명령어
        
    os.system(cmd)  # 명령어 실행
    
def getContacts(list):  # 리스트를 받아서 출력함수
    for i, item in enumerate(list):
        print(f'{i+1}=====>')
        print(item)
    
def run():
    # 연락처를 담을 주소록 리스트 생성
    listContact = []
    loadContact(listContact)    # 연락처 로드
    
    clearConsole()  # 화면을 클리어
    while True:
        selMenu = displayManu()
        if selMenu == 1:    # 연락처 추가인 경우
            clearConsole()
            try:
                contact = setContact()
            except: # 입력을 시킨대로 안하면
                contact = None
                
            if contact != None:
                listContact.append(contact)
                input('입력 성공!')
            # print(listContact)
            else:
                input('입력 실패')  # 엔터를 입력하도록 유도
            clearConsole()
            
        elif selMenu == 2:  # 연락처 출력
            clearConsole()
            getContacts(listContact)
            input('출력 성공!')
            clearConsole()
            
        elif selMenu == 3:  # 연락처 삭제
            clearConsole()
            name = input('삭제할 이름 입력: ')
            delContact(listContact, name)
            input('삭제 성공!')
            clearConsole()
            
        elif selMenu == 4:
            saveContact(listContact)
            break
        # else:
        #     clearConsole()
    # setContact()
    # first = Contact('홍길동', '010-8532-4832', 'fswe@naver.com', '경성')      # 위의 순서와 맞게 입력
    # first = Contact(addr='경성', phoneNumber='010-8532-4832', name='홍길동', eMail='fswe@naver.com')
    # print(first)
    
if __name__ == '__main__':  # 메인트리
    print('프로그램 시작')
    run()   #메인함수 실행

print('프로그램 종료')
