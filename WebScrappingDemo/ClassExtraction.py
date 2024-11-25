import requests
from bs4 import BeautifulSoup

url= "https://realpython.com/"
response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')
#print(soup)

# Get the text of class
card_title_tags = soup.find_all(class_='card-title')
for title in card_title_tags:    
    print(title)