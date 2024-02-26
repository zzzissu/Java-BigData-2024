# file : p25_usingModule.py
# desc : 모듈 사용

import calc     # calc.py를 사용한다는 의미    # {} : 패키지 이거나 모듈이라는 의미
# import calc as n으로 이름을 바꿀 수 있음(n 부분에 원하는 이름)

# from calc import mul을 사용하면 아래에서 > calc.mul()을 mul()로만 사용할 수 있음(함수명 충돌 주의)
# from calc import mul as mult(충돌이 우려 되면 이름 바꿔주기)

# print(__name__)     # 메인 엔트리, 가시적으로 전체 모듈이나 폴더 안에서 시작되는 포인트를 지정하고 싶을 때 사용
import Math
from day03.p22_carClass import Car  #디렉토리(모듈 묶음 : 패키지). 모듈명

if __name__ == '__main__': ## java void main()과 동일한 역할
    result = calc.mul(10, 7)
    print(result)
    
    myMath = Math.Math() # Math라는 모듈(파일) 이름, Math class이름을 써주어야 함 = 파일 이름과 class이름은 전혀 연관이 없음
    print(myMath.solv(10))
    # import Math를 > from Math import Math 로 사용하면(from Math(Math 파일에 있는~) import Math (class Math를 사용하겠다))
    # myMath = Math()로 사용 가능

