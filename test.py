from selenium import webdriver
import cv2
import numpy as np
import time
URL = "https://streamlabs.com/alert-box/v3/FCA342A8953B82476CF1"
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
config = {i.split(":")[0]: i.split(":")[1][:-1] for i in open("config").readlines()}
"""while True:
    #driver.get(f"https://streamlabs.com/alert-box/v3/{config['access_token']}")
    driver.get(URL)
    driver.save_screenshot("screen_shot.png")
    img = cv2.imread("screen_shot.png", 0)
    cv2.imshow("Alert", img)
    cv2.imshow("Alert Box", np.array(img))
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break"""
#driver.get(f"https://streamlabs.com/alert-box/v3/{config['access_token']}")
driver.get(URL)
time.sleep(7)
driver.save_screenshot("screen_shot.png")