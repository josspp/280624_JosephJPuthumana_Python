from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

# Geckodriver file path
driver_path = os.getcwd() + '/Selenium/MozillaDriver/geckodriver.exe'
screenshotPath = os.getcwd() + '/SeleniumProject/'

service = Service(driver_path)
driver = webdriver.Firefox(service=service)
driver.maximize_window()
# Navigating into the URL
driver.get("https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI")

# Find element
navElement = driver.find_element(By.ID,"advchart")
driver.implicitly_wait(5)
time.sleep(5)

# Saving the screenshot of the element
navElement.screenshot(screenshotPath + 'RI_ChartElement.png')
driver.implicitly_wait(3)

# Scrolling to the Element
actions = ActionChains(driver)
actions.scroll_to_element(navElement)

# Taking the page screenshot
driver.implicitly_wait(5)
time.sleep(5)
driver.save_screenshot(screenshotPath + "RI_ChartNavigated.png")

# Putting delay to close
time.sleep(10)
driver.quit()