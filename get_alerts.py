from selenium import webdriver
from pytesseract import image_to_string
from PIL import Image

import cv2
import numpy as np
import time
import random
import pyttsx3

#config = {i.split(":")[0]: i.split(":")[1][:-1] for i in open("config").readlines()}
#URL = f"https://streamlabs.com/alert-box/v3/{config['access_token']}"
URL = "https://streamlabs.com/alert-box/v3/2455D9407A647607A464"
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
driver.get(URL)

while True:
    driver.save_screenshot("shot.png")
    img = cv2.imread("shot.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(image_to_string(gray))
    time.sleep(0)
