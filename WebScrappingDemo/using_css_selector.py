import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com"


response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

#quote_object = soup.find(class_="quote")
#text_object=quote_object.find(class_="text")
#print(text_object.text.strip())

#author_object=quote_object.find(class_="author")
#print(author_object.text.strip())

quotes =soup.select(".quote .text")
authors = soup.select(".quote .author")


for each_quote, each_author in zip(quotes,authors):
    print(each_quote.text," - ",each_author.text)


with open("quotes.txt", "w") as file:
    # Loop through each quote and author, and write them to the file
    for each_quote, each_author in zip(quotes, authors):
        file.write(f'"{each_quote.text.strip()}" - {each_author.text.strip()}\n')

print("Quotes have been written to 'quotes.txt'")