import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to fetch movie details using Selenium
def movie_rating(userinput_moviename):
    movie_name = None
    director = None
    rating = None
    
    driver_path = "geckodriver.exe"  # or specify the full path to your geckodriver
    service = Service(driver_path)
    
    # Initialize the Firefox WebDriver
    driver = webdriver.Firefox(service=service)
    driver.get("https://www.imdb.com/")

    # Locate the search box and input the movie name
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(userinput_moviename)
    search_box.send_keys(Keys.RETURN)

    try:
        # Wait for the first movie result to load and click it
        movie_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@class='findSectionHeader']//following-sibling::table//tr[1]//td[@class='result_text']/a"))
        )
        movie_link.click()
        
        # Wait for the movie page to load
        time.sleep(5)

        # Extract the movie details
        movie_name = driver.find_element(By.XPATH, "//h1[contains(@class, 'TitleHeader')]").text
        rating = driver.find_element(By.XPATH, "//span[contains(@class, 'sc-16ede09-2')]").text
        director = driver.find_element(By.XPATH, "//span[text()='Director:']//following-sibling::a").text

    except Exception as e:
        print(f"Error while fetching movie details: {e}")
    
    driver.quit()
    
    return movie_name, director, rating

# Function to write movie details to a file
def write_to_file(movie_name1, rating_1, director_1, filename="movies_rating.txt"):
    if movie_name1 and rating_1 and director_1:
        # Open the file in append mode and write the movie details
        with open(filename, 'a') as file:
            file.write(f"Movie name: {movie_name1}\n")
            file.write(f"Movie rating: {rating_1}\n")
            file.write(f"Movie director: {director_1}\n")
            file.write("***************\n")
        st.success(f"Successfully written to {filename}")
    else:
        st.error("No valid outputs to write.")

# Streamlit User Interface
def myMenu():
    st.title("Movie Review Fetcher")

    # Dropdown for movie selection
    movie_list = ["Inception", "The Dark Knight", "Tenet", "The Matrix", "Interstellar"]  # You can expand this list
    selected_movie = st.selectbox("Choose a movie:", movie_list)
    
    # Input for custom movie name
    custom_movie = st.text_input("Or enter a movie name:")
    
    # If a movie is selected or a custom movie is entered, fetch details
    if selected_movie or custom_movie:
        if selected_movie:
            movie_name_input = selected_movie
        else:
            movie_name_input = custom_movie
        
        if st.button("Get Movie Details"):
            with st.spinner("Fetching movie details..."):
                movie_name, director, rating = movie_rating(movie_name_input)
                
                if movie_name and director and rating:
                    st.subheader("Movie Details")
                    st.write(f"**Movie Name:** {movie_name}")
                    st.write(f"**Rating:** {rating}")
                    st.write(f"**Director:** {director}")
                    
                    # Option to write details to a file
                    if st.button("Write to File"):
                        write_to_file(movie_name, rating, director)
                else:
                    st.error("Could not fetch movie details.")
    
    # Option to exit
    if st.button("Exit"):
        st.write("Exiting the application.")

if __name__ == "__main__":
    myMenu()
