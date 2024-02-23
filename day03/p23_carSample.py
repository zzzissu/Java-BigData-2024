# file : p23_carSample.py
# desc : Car 클래스 사용해보기

from p22_carClass import Car    # carClass에서 Car 상속받기

myCar = Car('87하 6213')   # 클래스를 사용, 객체를 하나 생성(instance)
yourCar = Car('22루 6854')
# print(myCar)
# print(yourCar)
myCar.__carNum = '54라 9835'        # 사용 불가
myCar.company = '현대자동차'
myCar.fuelType = '가솔린'
myCar.carType = '하이브리드'
myCar.color = '흰색'
myCar.releaseYear = '2018'

yourCar.__carNum = '98호 5423'      # 사용 불가
print(myCar)        # 객체에 대한 설명


myCar.start()
myCar.accel()
myCar.turnLeft()
myCar.turnRight()
myCar.breke()
myCar.getCarColor()

yourCar.start()