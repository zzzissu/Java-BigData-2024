# file : p54_captWeather.py
# desc : 네이버 날씨화면 캡쳐

import pyautogui as auto

import pyperclip as clip
import time

# auto.mouseInfo()

regions = ['서울', '강원', '대전', '대구', '부산']

for region in regions:
    # auto.moveTo(270, 270, duration=0.5) # 메인화면 기준
    auto.moveTo(460, 150, duration=0.5) # 검색화면 기준
    auto.leftClick()
    for _ in range(7):
        auto.press('backspace')
    time.sleep(0.2)

    clip.copy(f'{region} 날씨')
    auto.hotkey('ctrl', 'v')
    time.sleep(0.2)

    auto.press('\n')    # enter도 가능
    time.sleep(1.0)


    startX, startY = 130, 235
    endX, endY = 810, 860
    auto.screenshot(f'./day08/{region}날씨.png', region=(startX, startY, endX-startX, endY-startY))

    print('저장완료!')
    
    # im = auto.screenshot(region=(startX, startY, endX-startX, endY-startY))
    # im.save(f'./day08/{region}날씨.png')
    # mac OS버전은 위와 같이 설정