# file : p16_io.py
# desc : 입출력 학습

# input() 함수 기본
#res = input('인사말을 적으세요 > ')
#print(res)

num = input('곱할 수를 적으세요 > ')
print(type(num))
# input() 으로 받는 값은 모두 문자열
num = int(num)
print(num * 2)              # 문자열에는 /, - 불가능
# 숫자를 입력받아서 계산 등을 할 때에는 형 변환이 필요

num = int(input('2로 곱할 숫자 입력 > '))       # 정수만 가능(실수, 문자, 특수문자 모두 불가능)
print(num*2)

## 여러값 입력
int(40.2)   # 40
int('50')   # 50
int((10, 20, 30))   # 튜플을 바로 int로 변경할 수 있는 방법이 없음

# 첫 번째 방법
(a1, a2, a3) = input('세 값을 입력(구분자 space) > ').split(' ')
print(a1, a2, a3)
# .split = input()의 여러개의 값을 입력할 때 입력을 구분할 수 있는 값을 입력
# .split(' ') >> .split(','), .split('>') 등등..모두 가능

# 두 번째 방법
# 튜플의 괄호 중 할당을 받는 쪽의 괄호()는 생략 가능
(a1, a2, a3) = map(int,input('세 값을 입력(구분자 space) > ').split(' '))
# (a1, a2, a3) = int(input('세 값을 입력(구분자 space) > ').split(' '))      (x)
# map =  input()의 값을 int형으로 변경하기 위함
print(a1)
print(a2)
print(a3)
sum = a1 + a2 + a3
print(f'합계는 {sum}')
