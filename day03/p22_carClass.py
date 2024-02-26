# file : p22_carClass.py
# desc : 객체 지향 클래스 학습

class Car:
    __carNum = ''   # __ 언더바 2개 = private / 언더바 사용하지 않으면 public
    company = ''
    releaseYear = 1960
    color = 'white'
    carType = ''
    fuelType = '가솔린'         # 명사(객체)

    def start(self):
        print(f'{self.__carNum}이(가) 시동을 겁니다')      
        # {}에 carNum을 삽입하면 지역변수가 되어버려서 self를 이용하여 입력
        
    def accel(self):
        print(f'{self.__carNum} 엑셀을 밟습니다')

    def breke(self):
        print(f'{self.__carNum}브레이크를 밟습니다')

    def turnLeft(self):
        print(f'{self.__carNum}좌회전합니다')

    def turnRight(self):
        print(f'{self.__carNum}우회전합니다')   # 동사(메소드)
        
    def getCarColor(self):
        print(f'{self.__carNum}은(는) {self.color}입니다')
    
    def __init__(self) -> None:       # 언더바 2개 : 생성자같은 역할 -> None: 리턴할게 없음
        print('Car 객체를 생성합니다.')
        
    def __str__(self) -> str:       # 객체 변수를 print()할 때 출력 커스터마이징 함수
        # init은 생성자이기 때문에 None, str은 스트링이기 때문에 str이라고 나옴
        return f'내 차는 {self.company}, {self.__carNum}입니다.'
    
    def __init__(self, carNum) -> None:
        self.__carNum = carNum
        print('Car 객체를 생성합니다.')
        
    def setCarNum(self, carNum) -> None:
        self.__carNum = carNum
        
    def getCarNum(self, carNum) -> str:
        return self.__carNum