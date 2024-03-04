# file : p52_screenCap.py
# desc : pyautogui로 화면 캡쳐하기

'''
> pip install pillow
'''

import pyautogui as auto
import time

startX, endX = 0, 1919
startY, endY = 0, 1079

auto.screenshot('./day08/screen.png', region=(startX, startY, endX-startX, endY-startY))
time.sleep(2.0) # 파일 저장 후 너무 빨리 읽으면 에러(시간 텀을 줘야함)

capImg = auto.locateOnScreen('./day08/screen.png')  # 이미지 로드
print(capImg)
auto.click(capImg)
