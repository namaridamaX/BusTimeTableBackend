import os
import shutil
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def Selenium_pdf():
    shutil.rmtree('PDF')
    os.mkdir('PDF')

    driver = webdriver.Chrome(service=Service('C:\Program Files\chromedriver.exe'))
    driver.get('https://www.chitose.ac.jp/info/access')
    time.sleep(1)

    file_url = driver.find_element(By.XPATH, "//*[@id='paragraph_107_1615971519']/div/div/div[1]/a").get_attribute("href")
    urllib.request.urlretrieve(file_url, "PDF/bus.pdf")
    time.sleep(1)

    driver.close()

