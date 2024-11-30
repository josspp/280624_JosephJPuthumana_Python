import requests
from bs4 import BeautifulSoup

url="https://w3schools.com/html/"


response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

header = soup.find(id="getdiploma")
print(header.text.strip())

