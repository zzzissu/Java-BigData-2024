# file: p05_dict.py
# desc: 딕셔너리 자료형 연습

## 딕셔너리 구성 = {key1 : value1, key2 : value2...}
spiderMan = {'name':'Peter Parker', 'age':18, 'weapon':'Web shooter', 'friends':['ironMan', 'Thor', 'Captain Amertca']}
print(spiderMan)

## 출력
print(spiderMan)
print(spiderMan['name'])

## 값 추가
spiderMan['job'] = 'CameraMan'
print(spiderMan)

## 값 삭제
del spiderMan['friends']
print(spiderMan)

## 딕셔너리 함수
print(spiderMan.keys()) # 딕셔너리에 현재 존재하는 키 목록
print(list(spiderMan.keys()))    # 키 목록을 리스트 형태로 형 변환
print(spiderMan.items())    # 딕셔너리 모든 아이템 출력
print(spiderMan.get('job')) # 딕셔너리의 값 가져오기 함수

print('friends' in spiderMan)   # 딕셔너리 안에 키가 있는지 확인
print(spiderMan.values())

res = spiderMan.pop('job')
print(res)
print(spiderMan.pop('age'))
print(spiderMan)

## 데이터 삭제
spiderMan.clear()
print(spiderMan)

## 완전 삭제
del spiderMan
print(spiderMan)

## 집합 : 중복허용하지 않음, 순서 없음
# set([1, 2, 3, 4, 5, 5, 4, 2, 1, ]) = {1, 2, 3, 4, 5} or {3, 5, 1, 2, 4}...순서가 없기 때문

