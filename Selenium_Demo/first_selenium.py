from selenium import webdriver
from selenium.webdriver.firefox.service import Service  # Corrected import

# Specify the path to geckodriver
driver_path = r"geckodriver.exe"

# Initialize the Service object with the path
service = Service(driver_path)

# Create the Firefox WebDriver instance
driver = webdriver.Firefox(service=service)

# Open Google
driver.get("https://www.twitter.com")

print("Title of paage is: ",driver.title)

# Wait for 10 seconds
import time
time.sleep(3)

# Quit the driver after the wait
driver.quit()
