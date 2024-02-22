# file : p10_forCondition.py
# desc : for 반복문

# for item in 반복할객체:
#   ...

a = [1, 2, 3]
for i in a:
    print(i)

# for i in [1, 2, 3]:       # 위와 같음.
#     print(i)

a = [1, 3, 5, 7, 9]
print(type(a))  # <class 'list'>

for i in ['one', 'two', 'three']:
    print(type(i))

b = [(1, 2), (3, 4), (5, 6)]    #tuple의 리스트
for i in b:
    print(type(i))

for(first, second) in b:    # 튜플의 괄호는 생략 가능(= for first, second in b: )
    print(first, second)

# 평균 내기
grade =  [90, 80, 50, 70, 10]
sum = 0
for i in grade:
    sum += i
print(sum)  # 총합
print(sum / len(grade)) # 평균

## range()
print(range(10))    # range(0, 10)을 생략형으로 작성
print(range(0, 10))
for i in range(0, 10):
    print(i, end = ', ')
print()
print(list(range(0, 10)))
print(list(range(0, 10+1, 2)))  # 0부터 짝수로 구해짐
print(list(range(1, 10+1, 2)))  # 1부터 홀수로 구해짐
print(list(range(10, 0, -2)))
print(list(range(4, 101, 4)))
print(list(range(10, 0, -1)))   # range(시작 숫자, 끝 숫자, (출력규칙=없으면 차례대로 1씩 증가))

res = 0
for i in range(1, 101):
    res += i
print(res)

## list comprehension\ 리스트 내포
# list(range()) 만으로도 리스트를 생성할 수 있지만, 여러조건으로 리스트 생성할 때는 list comprehension 더 유용
print([i for i in range(1, 1001)])  # range보다 조금 더 많은 조건으로 출력 가능
print(list(range(1, 1001)))
print([num * 3 for num in range(1, 1001) if num % 3 == 0])
