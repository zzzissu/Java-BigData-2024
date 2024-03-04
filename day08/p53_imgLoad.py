# file : p53_imgLoad.py
# desc : PyAutoGUI에서 이미지 읽어오기

import pyautogui as auto

auto.alert('테스트!', title= 'PyAutoGUI')
auto.confirm('계속 진행하시겠습니까?')

text = auto.prompt('원하는 메세지 입력')
print(text)

pwd = auto.password('암호 입력', mask = '*')    # mask는 암호를 *로 나타나게 해줌
print(pwd)
