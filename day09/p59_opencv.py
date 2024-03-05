# file : p59_opencv.py
# desc : OpenCV 활용

# OpenCV 실시간 이미지 프로세싱 라이브러리

'''
> pip install opencv-python
'''

import cv2

# print(cv2.__version__)  # OpenCV 설치 확인용

img = cv2.imread('./day09/coby.jpg', cv2.IMREAD_UNCHANGED)   # CV2.IMREAD_GRAYSCALE -> 컬러이미지를 흑백으로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 원본을 흑백으로 변경

height, width, channel = img.shape  # y축, x축, (R, G, B를 추출(3채널은 모든색, 0은 흑백))
print(width, height, channel)

sizeSmall = cv2.resize(img, (width//2, height//2))

img_cropped = img[:, :(width//2)]       # [y축(: = 전체라는 의미), x축]    # x축을 반으로 자르기(:콜론을 기준으로 ()괄호의 내용이 (): 또는 :() 으로 자를 위치 조정)
# img_cropped = img[:(height//2), (width//2):]

cv2.imshow('Coby the cat, color', img)  # ('창 이름(제목)',img)
cv2.imshow('Reducd Coby', sizeSmall)    # 사이즈 반으로 줄이기
cv2.imshow('Coby the cat, gray',gray)   # 흑백
cv2.imshow('Half Coby', img_cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
