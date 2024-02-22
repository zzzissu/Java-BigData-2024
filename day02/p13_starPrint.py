# file : p13_starPrint.py
# desc : 별찍기

# 제일 쉬운 방법
print('예제 그림------')
for i in range(1, 6):
    print('*' * i)
    
# 2중 for문으로 결과를 똑같이 만들기
print('\n')

print('별찍기---------')
for i in range(1, 6):   # 손댈 필요 없음
    for j in range(i, 6):   #range()안쪽만 손대면 끝
        print(' ', end='')  # end= = 옆으로 정리
    
    for j in range(6-i, 6): # 위 for문 없이 <<이 for문만 사용하면 왼쪽부터 출력
        print('*', end='')
    print()


for i in range(1, 6):
    for j in range(6-i, 6):
        print('*', end='')
    print()
    
