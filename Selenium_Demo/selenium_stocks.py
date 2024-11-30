from selenium import webdriver
from selenium.webdriver.firefox.service import Service  # Corrected import
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to geckodriver
driver_path = r"geckodriver.exe"

# Initialize the Service object with the path
service = Service(driver_path)

# Create the Firefox WebDriver instance
driver = webdriver.Firefox(service=service)

# Open Google
driver.get("https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI")


links=driver.find_elements(By.TAG_NAME,"a")
driver.implicitly_wait(20)

#print("Title of paage is: ",driver.title)


time.sleep(20)

# Quit the driver after the wait
driver.quit