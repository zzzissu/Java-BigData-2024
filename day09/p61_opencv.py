# file : p61_opencv.py
# desc : OpenCV (계속)

import cv2

img = cv2.imread('./day09/coby.jpg', cv2.IMREAD_UNCHANGED)
dst = cv2.blur(img, (5, 5), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
# blur(이미지 이름, (블러 강도), anchor=(), borderType(가장자리 처리)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
canny = cv2.Canny(img, 100, 255)

height, width, channel = img.shape

cv2.imshow('Coby the cat', img)
cv2.imshow('Blur', dst) # 블러 이미지
cv2.imshow('Sobel', sobel)  # 입체감 있는 윤곽
cv2.imshow('Laplacian', laplacian)  # 일반적인 윤곽
cv2.imshow('Canny', canny)  # 흑백으로 윤곽

cv2.waitKey(0)
cv2.destroyAllWindows()
