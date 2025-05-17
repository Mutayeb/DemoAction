from Selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from time import sleep

#selenium.open("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
driver=webdriver.Edge()
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(10)
dropdown=select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0) #will select option at 1st place in dropdown i.e., Male
print(dropdown.first_selected_option.text) #will print the selected option
print(driver.title)

time.sleep(10)
driver.quit()
