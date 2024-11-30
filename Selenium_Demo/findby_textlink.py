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


#link=driver.find_element(By.XPATH,"//a[contains(text(), 'most populous country')]")

#print("Link to text 'most populous country': ",link.get_attribute("href"))

link=driver.find_element(By.LINK_TEXT,"Zoroastrianism")
print("link is:",link)
print("link text is:",link.text)

driver.get(link.get_attribute('href'))

driver.implicitly_wait(20)

#print("Title of paage is: ",driver.title)


time.sleep(3)

# Quit the driver after the wait
driver.quit