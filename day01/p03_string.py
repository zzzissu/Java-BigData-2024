# file: p03_string.py
# desc: 문자열 자료형과 연산

a = "Hello World"
print(a)
b = 'Hello World'
print(b)
c = "Hello, 'Ashley'"
print(c)
# 역슬래시는 탈출문자 \n, \t 외 나머지는 파이썬에 잘 사용되지 않음

# 문장을 여러줄 쓰고 싶으면 \ 로..
d = 'Hello\n' \
'I\'m Hugo' \
'Nice to meet you'
print(d)
# 여러줄 문장을 쓸때는 ''', """
d = '''hello
I'm Ashley.     
Nice to meet you, too'''
print(d)

## 문자열 연산 +, *
before = 'I wanna go to'
after = 'Boracai'
print(before + after) # +는 문자열을 합쳐서 하나의 문자열을 만듬
print(after * 3) # *는 문자열을 몇번 반복

## 문자열 길이 구하기
print('글자 길이 = ', len(before))
print('한글 글자 길이', len('안녕하세요')) # 5

## 문자열 인덱싱, 슬라이싱
cp = 'Life is too short, you need Python'
print(len(cp))

##슬라이싱
print(cp[8])
print(cp[17])


# cp[8] = 'd' # 문자열은 배열이긴 하지만, 값을 변경할 수 없는 특수 배열
print(cp[12:16+1]) # :(콜론) 뒤에 잇는 숫자는 항상 +1

print(ascii('안'), ascii('녕'), ascii('하'), ascii('세'), ascii('요'))
print(chr(97))

# 기존 문자열로 새로운 문자열을 만들 때는 슬라이싱, 다른 문자열로 대체필수
print(cp[0:7+1], 'long', cp[17:]) # :(콜론) 뒤를 생략하면 끝까지 출력

# 다른언어에는 없는 -슬라이싱
print(cp[-6:-1]) # -1대신 0은 안됨, 
print(cp[-6:])
print(cp[-11:-7]) # - 로 슬라이싱때도 : 뒤에는 +1을 해줘야함

## 문자열 포맷팅(format string)
## 파이썬에서는 %d, %s, %c 등 포맷스트링용 연산자를 사용 빈도 낮음
temp = 21
print('현재 온도는 %d도 입니다.'% temp)
temp = 17
print('현재 온도는 %d도 입니다.'% temp)

## format 함수로 포맷팅(가장 일반적)
print('현재 온도는 {0}도 입니다.'.format(temp))

## 날짜를 포맷으로 만들때
month = 2
day =21
hour = 3
mins = 18
print('오늘은 {0:02d}-{1:02d}, {2:02d}:{3:02d}분 입니다.'.format(month, day, hour, mins))

# 숫자 자료형
intcome = 7_000_000_000 #연매출
print('올해 매출액은 {0:,d}원'.format(intcome))
PI = 3.1415926536
print('파이는{0:10.2f}'.format(PI)) # 10.2f 소수점 .까지 다 포함해서 10자리, 소수점뒤는 2자리
# print('{0:d}'.format(PI)) # 실수형은 d(정수형 포맷팅) 불가 # 예외처리

## f 포맷팅 3.6 (2016)이후에 나온 최신방식
name = '홍길동'
age = 30

cont = f'나는 {name}이고, 나이는 {age}세 입니다.'   #f없으면 안됨
print(cont)
name = '한지수'
age = 27
print(f'나는 {name:>10}이고, 나이는 {age:03d}세 입니다.')   #03d = 세 자리 수를 만들되, 빈자리는 0으로 채움
print(f'나는 {name:<10}이고, 나이는 {age:03.1f}세 입니다.') 
#정수는 f포맷 사용가능, 실수는 d포맷 사용불가

## 문자열 함수
a = 'Life is short, You need Python'

print(a.count('Life'))  # count = 글자나 단어의 개수를 세어줌
print(a.count('o'))

print(a.find('sh')) # find = 해당 글자가 어디에 위치해 있는지 알려줌

print(a.index('t')) # index = 첫번째 t의 위치를 알려줌
#print(a.index('k'))    # index는 count를 조회 했을 때 개수가 0이 아닐때만 호출
print(','.join('abcde')) # 글자 사이마다 ''안의 문자를 삽입

print(a.upper())    # 영어를 대문자로 바꿔줌
print(a.lower())    # 영어를 소문자로 바꿔줌
print(a.capitalize())   #문장 첫 글자만 대문자로 바꿔줌

origin = '         Hi          '
print(f'++{origin}++')
print(f'++{origin.lstrip()}++')     # 왼쪽 공백 없애기
print(f'++{origin.rstrip()}++')     # 오른쪽 공백 없애기
print(f'++{origin.strip}++')      # 양쪽 공백 없애기        #글자 사이의 공백은 불가능, 문장의 맨 앞, 맨 뒤만 가능

print(cp.replace('too', '').replace(' short', 'long'))

## 문자열 자르기 -> 리스트(파이썬에는 배열이 없음)
cpWords = cp.split(' ')
print(cpWords)      # 한 문장이 스페이스 기준으로 잘려서 배열이 됨
