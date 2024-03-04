# file : p50_mouseAuto.py
# desc : PyAutoGUI로 마우스 조작

'''
파이썬 모듈 설치 시에 명령프롬포트보다 VS Code 내의 터미얼에서 설치를 추천(대부분 재시작하지 않아도 됨)
PyAutoGUI 모듈 설치
> pip install pyautogui
'''

import pyautogui as auto

print(auto.size())  # 모니터 해상도 정보 Size(width=1920, height=1080)
print(auto.position())  # 마우스 현재 위치

# pyautogui 마우스설정 창
# pillow 모듈이 같이 설치되어야 색상 표시가능
# auto.mouseInfo()

## 마우스 이동(절대 좌표) moveTo
auto.moveTo(100, 51)    # (0, 0)은 이후 이동 안됨
auto.moveTo(590, 105, duration=1.0) # x축 590, y축 105으로 1.0초 동안 이동
auto.moveTo(1210, 560, duration=0.1)

## 마우스 이동(상대좌표) move
# auto.move(50, 50, duration=1.5) # 현재 마우스 위치에서 x축 50, y축 50으로 1.5초 동안 이동

## 마우스 클릭
# auto.leftClick()    # 해당 위치로 가서 바로 왼쪽버튼 클릭
# auto.rightClick(x=790, y=300)   # 해당 위치로 가서 바로 오른쪽버튼 클릭
auto.click(clicks=4, interval=0.1, button='left')   # 왼쪽버튼을 소스코드 에디터에서 네번 클릭하면 모든 내용을 전체 선택가능

## 마우스 드래그
auto.leftClick(x=1300, y=300, duration=1.0) # 1300, 300위치에서 왼쪽마우스 클릭 후 1초 대기 했다가
auto.dragTo(x=500, y=640, duration=2.0, button='left')  # 드래그 함

auto.dragRel(500, 400, duration=1.0, button='left') # 현재위치에서 500, 400으로 1초 동안 드래그

## 마우스 휠
auto.scroll(1000)   # 양수는 위로
auto.scroll(-300)   # 음수는 아래로
