# file : p27_ExceptionHandle2.py
# desc : 예외처리 2
# 비정상적인 종료를 막기 위해 사용

# while True:
#     try:
#         select = input('메뉴입력 1. 저장 2. 검색 3. 종료 > ')
#     except:
#         print('예외가 발생했습니다. 입력을 정확히 하세요')
#         continue

#     if select == '1':
#         print('입력')
#     elif select == '2':
#         print('검색')
#     elif select == '3':
#         break
#     else:
#         continue
    
    #select = int(input('메뉴입력 1. 저장 2. 검색 3. 종료 > '))

    # if select == 1:
    #     print('입력')
    # elif select == 2:
    #     print('검색')
    # elif select == 3:
    #     break
    # else:
    #     continue      # int로 지정 시 문자를 삽입했을 때 오류가 남
    
class Chicken:
    def fly(self):
        raise NotADirectoryError
    
koko = Chicken()
try:
    koko.fly()
except Exception as e:
    print('닭은 못날아요', e.args)  # NotADirectoryError는 추가 예외메세지가 없음