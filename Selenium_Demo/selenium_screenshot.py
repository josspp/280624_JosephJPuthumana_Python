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
driver.get("https://en.wikipedia.org/wiki/India")
driver.implicitly_wait(3)
driver.save_screenshot("indiapage.png")


link=driver.find_element(By.LINK_TEXT,"Zoroastrianism")
driver.get (link.get_attribute('href'))
driver.implicitly_wait(3)
driver.save_screenshot("zoropage.png")



time.sleep(7)
#print("Title of paage is: ",driver.title)
# Quit the driver after the wait
driver.quit