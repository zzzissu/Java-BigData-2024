# file : p35_addrbook.py
# desc : 콘솔 주소록 프로그램

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
    
def run():
    # first = Contact('홍길동', '010-8532-4832', 'fswe@naver.com', '경성')      # 위의 순서와 맞게 입력
    first = Contact(addr='경성', phoneNumber='010-8532-4832', name='홍길동', eMail='fswe@naver.com')
    print(first)

    
if __name__ == '__main__':  # 메인트리
    print('프로그램 시작')
    run()   #메인함수 실행

print('프로그램 종료')
