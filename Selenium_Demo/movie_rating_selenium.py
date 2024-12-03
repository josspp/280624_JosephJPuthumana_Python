"""create a menu driven program to take a movie name from the user and get its rating, director name using selenium from an online source like IMDB 
The menu should have options for getting rating, writing all ratings to a file,
when he presses for quit the program you need to write all the movies and ratings that the user asked in the session to a file

tips:
1.create component wise, for eg: first create a selenium program to do this and then make it menu driven
2.Later write to a file
3.Store all searches in a cotainer(list/dictionary) and then write to a file"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to fetch movie rating and director from IMDb
def get_movie_info(movie_name):
    # Set the path to geckodriver (Ensure it's in your PATH or specify full path)
    driver_path = "geckodriver.exe"  # or specify the full path to your geckodriver
    service = Service(driver_path)
    
    # Initialize the Firefox WebDriver
    driver = webdriver.Firefox(service=service)
    
    # Navigate to IMDb
    driver.get("https://www.imdb.com/")
    
    # Find the search box and enter the movie name
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(movie_name)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the first movie result to appear
    try:
        # Wait for the search results to load and click on the first result
        #first_result = WebDriverWait(driver, 10).until(
        #    EC.presence_of_element_located((By.CSS_SELECTOR, ".findResult a"))
        #)
        #first_result.click()

        # Wait for the movie page to load
        #WebDriverWait(driver, 10).until(
        #    EC.presence_of_element_located((By.CLASS_NAME, "TitleBlock__TitleLink-sc-1nlhx7j-0"))
        #)
        time.sleep(5)
        movie_name = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]/div[2]")
        movie_name.click()
        time.sleep(3)

        # Extract the movie's rating
        try:
            rating = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]/div[1]").text
        except:
            rating = "Not Available"

        # Extract the director's name
        try:
            director = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/div[2]/div/ul/li[1]/div/ul/li/a").text
        except:
            director = "Not Available"

        driver.quit()
        return rating, director
    except Exception as e:
        print(f"Error occurred while fetching data for '{movie_name}': {e}")
        driver.quit()
        return None, None
    

# Movie ratings storage
movie_data = []

# Function to display the menu
def display_menu():
    print("\nMovie Rating System Menu:")
    print("1. Get Movie Rating")
    print("2. Write Ratings to File")
    print("3. Quit")
    choice = input("Enter your choice: ")
    return choice

# Function to save data to a file
def write_to_file():
    if movie_data:
        with open("movie_ratings.txt", "w") as file:
            for movie, rating, director in movie_data:
                file.write(f"Movie: {movie}, Rating: {rating}, Director: {director}\n")
        print("Movie ratings have been saved to 'movie_ratings.txt'.")
    else:
        print("No data to save.")

# Menu-driven program
def menu_program():
    while True:
        choice = display_menu()

        if choice == "1":
            movie_name = input("Enter the movie name: ")
            rating, director = get_movie_info(movie_name)
            
            if rating and director:
                movie_data.append((movie_name, rating, director))
                print(f"Movie: {movie_name}, Rating: {rating}, Director: {director}")
            else:
                print(f"Could not find information for '{movie_name}'.")

        elif choice == "2":
            write_to_file()

        elif choice == "3":
            write_to_file()
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")
    



# Run the program
if __name__ == "__main__":
    menu_program()
