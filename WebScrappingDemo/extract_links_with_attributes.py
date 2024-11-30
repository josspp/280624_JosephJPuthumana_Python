import requests
from bs4  import BeautifulSoup

url="https://www.python.org"

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

links = soup.find_all("a",href=True)

for link in links:
    if link['href'].startswith("https://pyfound.blogspot.com"):
        print(link["href"])