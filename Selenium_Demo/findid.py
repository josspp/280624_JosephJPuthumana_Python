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


#search_box=driver.find_element(By.ID,"username")
#search_box.send_keys("student")

#search_box=driver.find_element(By.ID,"password")
#search_box.send_keys("Password123")

#search_box=driver.find_element(By.ID,"submit")
#search_box.send_keys(Keys.RETURN)

links=driver.find_elements(By.TAG_NAME,"a")

count=1
for link in links:
    
    url=link.get_attribute("href")
    if url:
        print(url)
        count=count+1
    if count==30:
        break

driver.implicitly_wait(20)

#print("Title of paage is: ",driver.title)


time.sleep(20)

# Quit the driver after the wait
driver.quit