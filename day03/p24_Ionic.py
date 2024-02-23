# file : p24_Ionic.py
# desc : 클래스 상속

from p22_carClass import Car

class Ioinc(Car):   # Car 클래스를 상속 받아서 ioinc
    __fuelRate = 0.0    # 연비
    
    def setFuelRate(self, rate):
        self.__fuelRate = rate
        
    def getFuelRate(self) -> float:
        return self.__fuelRate
    
    def getCarNum(self) -> str:     # 함수 오버라이딩(재정의)
        
        return f'소중한 제 차는 {super().__carNum} 입니다'
    
myCar = Ioinc('54라 4863')
myCar.company = '기아자동차'
myCar.setFuelRate(23.5)
print(myCar)
print(f'내 차의 연비는 {myCar.getFuelRate()}km/l 입니다')
print(myCar.getCarNum())