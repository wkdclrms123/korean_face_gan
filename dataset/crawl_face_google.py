from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

a = input("키워드 : ")
b = int(input("개수 : "))
driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
driver.get('http://www.google.co.kr/imghp?hl=ko')
elem = driver.find_element_by_name("q")
elem.send_keys(a)
elem.send_keys(Keys.RETURN)
images = driver.find_elements_by_class_name("Q4LuWd")
count = 0
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_class_name("n3VNCb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, "imgfile/" + a + str(count) + ".jpg")
        count += 1
        if count >= b:
            break
    except:
        print('except')
        pass

driver.close()