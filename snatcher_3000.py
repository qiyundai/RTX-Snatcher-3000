from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys

options = Options()
options.headless = True
#options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)

driver.get("https://www.nvidia.com/en-us/shop/geforce/gpu/?page=1&limit=9&locale=en-us&category=GPU&gpu=RTX%203080")

a = driver.find_element_by_xpath('//*[@id="resultsDiv"]/div/div[1]/div[2]/div[3]/div[2]/div[1]/a')

buy_now = a.text
print(buy_now)

driver.quit()