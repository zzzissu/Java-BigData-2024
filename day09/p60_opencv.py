# file : p60_opencv.py
# desc : OpenCV 이미지 처리(계속)

import cv2

img = cv2.imread('./day09/coby.jpg', cv2.IMREAD_UNCHANGED)  # 원본
dst = cv2.flip(img, 0)  # (0)상하 반전 / (1) 좌우 반전

height, width, channel = img.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)    # 세번째 옵션, scale 1 = CCW 반시계 반향 / -1 = CW 시계 방향 / 2 = 배율
thrd = cv2.warpAffine(img, matrix, (width, height))

reverse = cv2.bitwise_and(img)  # 역상, 반전색
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, bny = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) # 이진화(0 또는 1)

cv2.imshow('Coby the cat, color', img)
cv2.imshow('Flip', dst)
cv2.imshow('Rotation', thrd)
cv2.imshow('Reverse', reverse)
cv2.imshow('Gray', gray)
cv2.imshow('Binary', bny)

cv2.waitKey(0)
cv2.destroyAllWindows()
