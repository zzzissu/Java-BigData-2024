# file : p34_addrBook.py
# desc : 콘솔 주소록 프로그램

import os # OS에서 필요한 모듈

class Contact: # 주소록 클래스
  # 생성자
  __name = ''
  __phoneNumber = ''
  __eMail = ''
  __addr = ''

  def __init__(self, name, phoneNumber, eMail, addr) -> None:
    self.__name = name
    self.__phoneNumber = phoneNumber
    self.__eMail = eMail
    self.__addr = addr

  # 사용자가 원하는 형태로 출력
  def __str__(self) -> str:
     res = (f'이  름 : {self.__name}\n'
            f'핸드폰 : {self.__phoneNumber}\n'
            f'이메일 : {self.__eMail}\n'
            f'주  소 : {self.__addr}\n')
     return res
  
  # 연락처 여부 확인
  def isNameExist(self, name):
    if self.__name == name: # 찾는 이름 존재
      return True
    else:
      return False
  
  def getInfo(self):
    return self.__name, self.__phoneNumber, self.__eMail, self.__addr
  
  
def setContact(): #사용자 입력으로 주소록 받기함수
  (name, phoneNumber, eMail, addr) = input('주소록 입력(이름, 핸드폰, 이메일, 주소[구분자 /]) >').split('/')
  name = name.strip()
  phoneNumber = phoneNumber.strip()
  eMail = eMail.strip()
  addr = addr.strip()
  #print(f'"{name}", "{phoneNumber}", "{eMail}", "{addr}"')
  contact = Contact(name, phoneNumber, eMail, addr) # 매개변수명과 동일하게 로컬변수 이름 지정
  return contact

def clearConsole():
  cmd = 'clear' #mac OS, Linux, Unix 명령어
  if os.name in ('nt', 'dos'): # window
    cmd = 'cls' # window 명령어
  os.system(cmd) # 명령어 실행

def delContact(lst, name): # 연락처 삭제함수
  for i, item in enumerate(lst):
    if item.isNameExist(name):
      del lst[i]

def saveContact(lst): # 연락처 저장함수
  with open('./contacts.txt', mode='w', encoding='utf-8') as fp:
    for item in lst:
      name, phoneNumber, eMail, addr = item.getInfo()
      fp.write(f'{name}/{phoneNumber}/{eMail}/{addr}\n')

def loadContact(lst): # 처음 실행시 데이터 읽어오는 함수
  with open('./contacts.txt', mode='r', encoding='utf-8') as fp :
    while True:
      line = fp.readline()
      if not line: break

      lines = line.replace('\n','').split('/')
      contact = Contact(name=lines[0], phoneNumber=lines[1], eMail=lines[2], addr=lines[3])
      lst.append(contact)


def displayMenu():
  menu = ('주소록 프로그램\n'
          '1. 연락처 추가\n'
          '2. 연락처 출력\n'
          '3. 연락처 삭제\n'
          '4. 종료\n')
  print(menu)
  sel = int(input('메뉴입력 : '))
  return sel

def getContacts(lst): # 리스트를 받아서 출력
  for i, item in enumerate(lst):
    print(f'{i+1} ==========> ')
    print(item)

def run():
  #연락처를 담을 주소록 리스트 생성
  lstContact = []
  loadContact(lstContact) # 연락처 로드

  clearConsole() # 화면을 클리어
  while True:
    selMenu = displayMenu()
    if selMenu == 1: # 연락처 추가
      clearConsole()
      contact = setContact()
      lstContact.append(contact)
      #print(lstContact)
      input() #엔터 입력 유도
      clearConsole()
    elif selMenu == 2: # 연락처 출력
      clearConsole()
      getContacts(lstContact)
      input(); clearConsole()
    elif selMenu == 3: # 연락처 삭제
      clearConsole()
      name = input('삭제할 이름 입력 : ')
      delContact(lstContact, name)
      clearConsole()
    elif selMenu == 4: # 프로그램 종료
      saveContact(lstContact)
      break

if __name__ == '__main__': # 메인엔트리
  print('프로그램 시작')
  run() #메인함수 실행

print('프로그램 종료')