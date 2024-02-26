# file : p29_builtinFunc.py
# desc: 내장함수

## abs(absolute) 절대값
print(abs(-5))

## all 현재 (반복 가능한)컬렉션 데이터의 조건이나 값이 참인 값만 있는지 확인
print(all([1, 2, 3, (4 < 2), 5]))

## chr() 아스키나 유니코드 값을 받아서 글자로 변경
print(chr(65))
print(chr(44032))

## ascii() 영문자, 문자를 아스키 숫자나 유니코드 숫자로 변경해줌
print(ascii('가'))

## dir() 객체가 지닌 변수, 함수를 알려주는 함수
print(dir(list()))
a = [1, 2]
a. append(3)
print(a)
val = a. pop()
print(val)

print(dir(dict()))      # 등등...

## divmod() 나누기의 몫, 나머지를 한번에 구해주는 함수
print(divmod(7, 2)) # = (3, 1)

## ★enumerate() : 열거하다는 뜻, 데이터 포함 인덱스를 같이 생성해주는 역할
for i in ['Hello', 'World', 'python']:
    print(i)

for (i, data) in enumerate(['Hello', 'World', 'python']):       # 값이 어디에 위치해 있는지 알려줌
    print(f'{i}번째 값은 {data}입니다')
    
## eval(evaluate): 실행함수, 문자열로 된 수식이나 함수를 실행해주는 역할
print(eval('divmod(10,3)'))

## hex: 10진수를 16진수로
print(hex(255)) #0xff       # hex(255).upper() = 대문자로 출력

## ★map: 여러 값을 한꺼번에 같은 조건으로 변경할 때
def ttime(x):
    return x*2

print(list(map(ttime, [1, 3, 5, 7, 9])))    # map을 써서 반복데이터를 ttime() 함수로 처리
print(list(map(int, [1.0, 2.0, 3.0, 4.4]))) # map을 써서 반복데이터를 int로 바꾸어 처리

# max()
print(max([3, 9, 99]))
print(min([3, 9, 99]))

## oct() 8진수
print(oct(34))

## ord() == ascii()
print(ord('A'))
print(ord('가'))

## round() 반올림(이상징후 4.5도 4로 나옴)
print(round(4.51))  # 4.5 != 5
print(round(4.45, 1))

## sum() 반복되는 컬렉션 자료
print(sum(range(1, 101)))

## tuple() 다른 컬렉션을 튜플자료형으로 변경
print(tuple([1, 2, 3, 4, 5]))

## ★type() 변수, 데이터의 타입 리턴
print(type('Hello'))    # <class 'str'>
aa = [1, 2, 3, 4]
print(type(aa)) # <class 'list'>

## zip() 동일한 개수로 데이터를 묶어서 (튜플로)리턴
odd = [1, 3, 5, 7, 9]
even = [ 2, 4, 6, 8, 10]
total = list(zip(odd, even))    # 쌍이 맞아야 함.(데이터의 개수가 odd(5개), even(4개)일 경우 나머지는 버려짐)
print(total)
