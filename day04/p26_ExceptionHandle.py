# file : p26_ExceptionHandle.py
# desc : 예외처리

# f = open('./sanple.txt', mode = 'r', encoding='urf-8')
# res = readline()
# print(res)
# f.close()

# print(5 / 0)

# a, b = 5, 3

# if a > b:
#     print(True)
    
# 오류(Error): 소스코드 상에 빨간 밑줄은 (예외와 오류는 구분해야 함)
# 예외(Exception): 프로그램 실행 중에 생기는 오류(비정상적 종료)
# 1. 파일을 읽어서
try:
    f = open('./sanple.txt', mode = 'r', encoding='urf-8')
    res = f.readline()
    print(res)
except:
    print('파일오픈 예외발생')
else:   #오류가 없는 경우에만 수행
    f.close()
    
# finally:
    # try:    #try~ except는 다중으로 사용하면 성능에 별로 안좋다
    #     f.close() # f에 파일 객체 자체가 없어서 close()불가
    # except NameError as e:
    #     print('파일 오픈 실패')

# 2. 계산결과
try:
    print(5 / 0)
except ZeroDivisionError as e :
    print('나누기 예외발생', e.args)        # 뭐때문에 에러가 발생했는지 알려줌
    
    