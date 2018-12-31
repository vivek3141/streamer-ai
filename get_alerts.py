from selenium import webdriver
import cv2
import numpy as np
import time
config = {i.split(":")[0]: i.split(":")[1][:-1] for i in open("config").readlines()}
URL = f"https://streamlabs.com/alert-box/v3/{config['access_token']}"
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)