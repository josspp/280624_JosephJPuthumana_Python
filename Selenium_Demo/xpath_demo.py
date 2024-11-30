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
driver.get("https://www.wikipedia.org")
driver.implicitly_wait(3)


#links=driver.find_elements(By.TAG_NAME,"a")

#print("Title of paage is: ",driver.title)

search_box=driver.find_element(By.XPATH,"//input[@id='searchInput']")
search_box.send_keys("India")

search_button=driver.find_element(By.XPATH,"""//*[@id="search-form"]/fieldset/button""")
search_button.click()
driver.implicitly_wait(5)

heading = driver.find_element(By.XPATH,"//span[contains(text(),'India')]")
print(heading)

#time.sleep(20)

# Quit the driver after the wait
driver.quit