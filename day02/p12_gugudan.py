# file : p12_gugudan.py
# desc : 구구단 프로그램

x = 2
for i in range(1, 10):  # 1~ 9까지
    print(f'{x} x {i} = {x*i}')     # 2단
    
x = 3
for i in range(1, 10):  # 1 ~ 9까지
    print(f'{x} x {i} = {x*i}')     # 3단
print('-------------------')    # 하나씩 하면 번거롭기 때문에 이중 for문 사용


print('구구단 프로그램 v99')
for x in range(2, 10): # 2단 ~ 9단 까지
    print(f'{x}단 시작 ---------------')
    for y in range(1, 10): # 1 ~ 9 까지
        print(f'{x} x {y} = {x*y:2d}', end= '\t')       # :2d는 왼쪽 정렬
    print() # 아무런 내용 없이 엔터만 해줌