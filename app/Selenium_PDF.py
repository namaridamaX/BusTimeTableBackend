import os
import shutil
import time
import urllib.request
# import chromedriver_binary
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def Selenium_pdf():
    # selenium_URL = "http://selenium:4444/wd/hub"
    # shutil.rmtree('PDF')
    # os.mkdir('PDF')

    # driver = webdriver.Chrome(http://selenium:4444/wd/hub)
    # driver = webdriver.Remote(
    #     command_executor=os.environ[selenium_URL],
    #     desired_capabilities=DesiredCapabilities.CHROME.copy()
    # )
    # driver.get('https://www.chitose.ac.jp/info/access')
    # time.sleep(1)

    # file_url = driver.find_element(By.XPATH, "//*[@id='paragraph_107_1615971519']/div/div/div[1]/a").get_attribute("href")
    # urllib.request.urlretrieve(file_url, "PDF/bus.pdf")

    shutil.rmtree('PDF')
    os.mkdir('PDF')
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor='172.18.0.3:4444/wd/hub', options=options)
    driver.get('https://www.chitose.ac.jp/info/access')
    time.sleep(1)
    file_url = driver.find_element(By.XPATH, "//*[@id='paragraph_107_1615971519']/div/div/div[1]/a").get_attribute("href")
    urllib.request.urlretrieve(file_url, "PDF/bus.pdf")

    time.sleep(1)

    driver.close()

