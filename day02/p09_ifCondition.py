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