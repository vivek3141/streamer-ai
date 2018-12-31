from PIL import Image
from pytesseract import image_to_string
import cv2

img = cv2.imread("screen_shot.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)[800:937, 0:937]
while cv2.waitKey(0) & 0xFF != ord('q'):
    cv2.imshow("", gray)

print(image_to_string(gray))
