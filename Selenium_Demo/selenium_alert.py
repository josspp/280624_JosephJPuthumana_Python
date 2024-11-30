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
driver.get("https://demo.guru99.com/test/delete_customer.php")

search_box= driver.find_element(By.NAME,"cusid")
search_box.send_keys("rohit.r")
search_box.send_keys(Keys.RETURN)

alert=driver.switch_to_alert
alert.accept()

search_box.send_keys(Keys.RETURN)

driver.implicitly_wait(20)

driver.quit