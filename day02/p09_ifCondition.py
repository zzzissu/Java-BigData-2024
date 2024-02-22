# file : p09_ifCondition.py
# desc : if 제어문

Money = 3000

if Money >= 5000:
    # indentation(들여쓰기) tab = space 4개와 같음
    print('택시타고 가')
    print('부럽네')
elif Money < 500 and Money >= 2500:
    print('기사님 홈플러스 앞까지만 가주세요')
    print('집까지 걸어감')
else:
    print('걸어가')
    print('돈도 없는게..')
    
a, b, c, d = 10, 5, 7, 9
print(a >= b)   # true(1)
print(c > d)    # false(0)
print(a >= b and c > d) # false # 1 and 1 == 1 / 1 and 0 == 0 / 0 and 1 == 0 / 0 and 0 == 0
print(a >= b or c > d)  #true   # 1 or 1 == 1 / 1 or 0 == 1 / 0 or 1 == 1 / 0 or 0 == 0
## and 80% / or 20% 사용률

print(not(a >= b)) # flase

##print() end 옵션(많이 사용), sep옵션
print(1 in [1, 3, 5, 7, 9]) # []안의 값 중 1이 있는지 검사
print(1 in [1, 3, 5, 7, 9], end = ', ') # 다음 값과 붙혀서 출력(''안의 내용(,) 으로 구분)
print(6 in [1, 3, 5, 7, 9])

print('13579', '246810', sep = '.') # sep = 구분자

score = 60
# 파이썬에서는 조건 연산자를 잘 안씀
# (score >= 60) ? "sucess" : " failure"
print('success' if score >= 60 else 'falure')