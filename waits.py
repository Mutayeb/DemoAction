from Selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from time import sleep

#selenium.open("")
driver=webdriver.Edge()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(10)

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)

