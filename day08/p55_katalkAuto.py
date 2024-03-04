# file : p55_katalkAuto.py
# desc : 카톡PC에서 자동으로 메세지 보내기

import pyautogui as auto
import pyperclip as clip
import os
import time

katalkLoc = auto.locateOnScreen('./day08/findLoc.png')
print(katalkLoc)
clickPos = auto.center(katalkLoc)
auto.doubleClick(clickPos)
time.sleep(0.5)


clip.copy('안녕하세요.')
auto.hotkey('ctrl', 'v')
auto.press('\n')
