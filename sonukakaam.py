#j=18
#print(j%9)
from selenium import webdriver
import string
import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser

Path = "D:\webdriver\\chromedriver.exe"
driver = webdriver.Chrome(Path)
m=0
m=int(m)
while(m<=19):
 driver.execute_script("window.open('');")
 driver.switch_to.window(driver.window_handles[m])
 m=m+1
 driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc_5otXxWdkXt7-3Cu2nvkwuyt4Y1TMXFdw1gUFHfaUGfACOw/viewform")
 k = 0
 time.sleep(3)
 d = driver.find_elements_by_xpath("//div[@class='appsMaterialWizToggleRadiogroupOffRadio exportOuterCircle']")
 d1=driver.find_elements_by_xpath("//input[@type='text']")
 cv=0
 names=["Sachin Joshi","Ramesh Joshi","Pritam Joshi","Tanmay Joshi", "Tanay Joshi","Toshik Joshi","Sparsh Tiwari","Sarthak Vyas","Aniruddh Bhave","Milind Phalke","Vanshika Joshi","Yashweeta Pare","Saloni Khandari","Vishal Agnihotri","Simran Khandekar","Mansi Jaiswal","Hasnaat Ali","Rashmi Sharma","Aashi Sharma","Swaraj Katmore","Ketan Badwe","Suhani Agnihotri","Vishesh Somani","Nivesh Somani","Tulsi Jain","Nidhi Kamdekar","Sanskar Gupta","Ishan Soni","Shreya Sharma","Ritik Verma","Prasoon Joshi","Siddhartha Shukla","Ruchi Singh","Akshat Yadav"]
 bank=["ICICI Bank","HDFC Bank","Axis Bank","State Bank of India","Yes Bank","IndusInd Bank","Bank of Baroda"]
 mk=0
 for i in d1:
    mk=mk+1
    if mk==1:
     i.send_keys(names[m-1])
    else:
     pass
     # i.send_keys(random.choice(bank))
 for i in d:
     cv=cv+1
     k = k + 1
     if (k-1)%5==0 and k>=2*len(d)/3:
         i.click()
     else:
         pass
     if k<2*len(d)/3 and cv%4==0:
        i.click()






#driver.get("http://www.codebind.com/python/opencv-python-tutorial-beginners-smoothing-images-blurring-images-opencv/")
"""while(m<30):
 driver.execute_script("window.open('');")
 driver.switch_to.window(driver.window_handles[m])
 m=m+1
 driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeB8L7xfVXnN3rEUjAvkLwPN3AqLp0ozxUySOqA_yM1BGlCyA/viewform?vc=0&c=0&w=1")
 k = 0
 time.sleep(3)
 d = driver.find_elements_by_xpath("//div[@class='appsMaterialWizToggleRadiogroupOffRadio exportOuterCircle']")
 for i in d:
     k = k + 1
     j=[1,2,3,4]
     if k == int(random.choices):
         i.click()
         k = 0
     else:
         pass"""