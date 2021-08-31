from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup as bs
import time
import urllib.request
import os

def names():
    def urlopen_custom(req_custom):
        try:
            html = urlopen(req_custom)
        except HTTPError as e:
            print(e.headers["Retry-After"])
            if e.getcode() == 429:
                time.sleep(int(e.headers["Retry-After"]))
            html = urlopen(req_custom)
            print(e)

        return html


    BASE_URL = "https://namu.wiki"
    req = Request(BASE_URL+"/w/%EB%B0%B0%EC%9A%B0/%ED%95%9C%EA%B5%AD", headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen_custom(req)
    bsObject = bs(html, "html.parser")

    links = bsObject.find_all("a", {"class": "wiki-link-internal"})
    print(len(links))
    img_count = 0
    namelist = []


    for link in links:
        if link.get("title") == "배우" or link.get("class") == ["wiki-link-internal", "not-exist"]:
            continue
        
        namelist.append(link.get('title'))

    return namelist

name = names()
b = int(input("사람당 사진갯수 : "))
driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
driver.get('http://www.google.co.kr/imghp?hl=ko')
for a in name:
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
            urllib.request.urlretrieve(imgUrl, "dataset/imgfile/" + a + str(count) + ".jpg")
            count += 1
            if count >= b:
                driver.get('http://www.google.co.kr/imghp?hl=ko')
                break
        except:
            print('except')
            pass