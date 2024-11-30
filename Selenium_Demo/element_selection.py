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
driver.get("https://www.duckduckgo.com")


search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

print("Title of paage is: ",driver.title)


time.sleep(3)

# Quit the driver after the wait
driver.quit()
