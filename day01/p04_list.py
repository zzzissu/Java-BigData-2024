# file : p04_list.py
# desc : 리스트

## 파이썬에는 배열이 없다. 리스트로 대신함
even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

print(even)
print(even[4])      # 길이가 n일때 마지막 인덱스는 n-1
# print(even[5])        # 예외 발생

even[4] = 20
print(even)     # 리스트는 인덱스의 값이 변경 가능

datas = [123, 45.6, True, 'Hello', odd, None]       # 형타입을 지정하지 않기 때문에 어떤 자료형이든 리스트에 할당 가능
print(datas)

## 인덱싱, 슬라이싱
print(odd[2])
print(even[0] + odd[0])     #숫자를 더하면 합계가 나옴

cpWords = ['Life', 'is', 'short']
print(cpWords[0] + cpWords[2])      #문자를 더하면 연결해서 나옴

print(even[1:4])

## 2차원 리스트
#3행 4열
# [[1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10, 11, 12]]

d2Datas = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]


for i in d2Datas:
    print(i)
    
dm1col1 = [1, 2, 3, 4]
dm1col2 = [5, 6, 7, 8]
dm1col3 = [9, 10, 11, 12]
    
print([dm1col1, dm1col2, dm1col3])

# 리스트 연산은 문자열 연산과 동일    
print(even + odd)
print(odd * 2)


## 값 변경
even[3] = 10
print(even)

del even[2]     # 값 삭제
print(even)


## 리스트 함수
# append = 리스트 제일 뒤에 추가
even.append(30) #값 추가
print(even)

# insert 원하는 위치에 값 추가
even.insert(2, 6)   # 인덱스 2에 6을 삽입
print(even)

# 정렬
origin = [45, 23, 9, 17, 1, 5, 11, 3, 29, 30]

origin.sort()       # 오름차순(Ascending)
print(origin)
origin.sort(reverse=True) # 내림차순(Descending)
print(origin)

# 뒤집기
aa = ['a', 'f', 'e', 'b']
aa.reverse()

print(aa)

print(aa.count('a'))
print(aa.index('e'))

bb = [1, 3, 5, 6, 8, 3, 1]
bb.remove(3)        # 여러 개의 3 중에 맨 앞에 있는 3만 삭제
print(bb)

print(even.pop())   # pop = 제일 마지막 값을 빼냄
print(even.pop())   # 스택의 기능 append() 마지막에 값 할당, pop() 마지막 값 꺼내기
print(even)

## 튜플
# 리스트랑 동일. 단, 삭제, 편집 불가
tVal = (1, 3, 5, 7, 9)

# tVal[2] = 11      #튜플은 한 번 만들어지면 끝까지 그대로 사용해야함
# del tval[2]