# name = input("Enter your name:")
# age = input("Enter your age:")
# age = int(age)
# print("Hello",name, "your age is",age)
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Webdriver import chromdriver

Chrome_Driver = chromdriver.Chrome_Driver
driver = webdriver.Chrome(service=Service(Chrome_Driver))
driver.get("https://www.google.co.in/")
driver.maximize_window()
name = driver.find_element(By.NAME, "q")
name.send_keys("Lipun")
name.send_keys(Keys.RETURN)
time.sleep(3)
driver.close()
driver.quit()
