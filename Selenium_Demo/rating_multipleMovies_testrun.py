import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def myMenu():
    movie_name=None
    rating=None
    director=None
    
    while True:
        print("1. Get the movie rating")
        print("2. Write to file")
        print("3. Exit")
        userinput=input("Enter your choice:")
        
        
        
        if userinput=="1":
            movie_name,director,rating=movie_rating()
        elif userinput=="2":
            if movie_name and rating and director:
                 write_to_file(movie_name,rating,director)
        elif userinput=="3":
            print("Exiting the menu")
            break
        else:
            print("Invalid choice")
def movie_rating():
    movie_name=None
    director=None
    rating=None
    userinput_moviename=input("Enter movie name:")
    driver_path = "geckodriver.exe"  # or specify the full path to your geckodriver
    service = Service(driver_path)
    # Initialize the Firefox WebDriver
    driver = webdriver.Firefox(service=service)
    # Navigate to IMDb
    driver.get("https://www.imdb.com/")

    
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(userinput_moviename)
    search_box.send_keys(Keys.RETURN)

    try:
        time.sleep(5)
        movie_name_element = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]/div[2]")
        movie_name=movie_name_element.text
        print("Movie name is:",movie_name)
        movie_name_element.click()
        time.sleep(5)
        print("Movie name found and clicked")
#        movie_name=movie_name_element.text
        print("Movie name obtained")

    except Exception as e :
            print("Movie name not Available to click")

    try:
        rating = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]/div[1]").text
    except Exception as e:
            print("Movie rating not Available")
    
    try:
         director = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/div[2]/div/ul/li[1]/div/ul/li/a").text
        
    except:
         print("Movie director not Available")
    
    driver.quit()
    return movie_name,director,rating


def write_to_file(movie_name1, rating_1,director_1, filename="movies_rating.txt"):
    # Check if the outputs are valid
    if movie_name1 is not None and rating_1 is not None and director_1 is not None:
        # Open the file in write mode and write the outputs
        with open(filename, 'a') as file:
            file.write(f"movie name: {movie_name1}\n")
            file.write(f"movie rating: {rating_1}\n")
            file.write(f"movie director: {director_1}\n")
            file.write("***************\n")
        print(f"Successfully written to {filename}")
    else:
        print("No valid outputs to write.")
          
if __name__ == "__main__":
    myMenu()