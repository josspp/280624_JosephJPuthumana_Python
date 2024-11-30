import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the BBC News page
url = "https://www.bbc.com/news"

# Send the GET request
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text,"html.parse")

# Find all the relevant headlines based on the h2 tag and the data-testid attribute
headlines = soup.find_all('h2', {'data-testid': 'card-headline'})

# Extract the text from each headline
headline_texts = [headline.text.strip() for headline in headlines if headline.text.strip()]

# Create a DataFrame
df = pd.DataFrame(headline_texts, columns=["Headline"])

# Write the DataFrame to a CSV file
df.to_csv('bbc_trending_headlines.txt', index=False)

print("Headlines have been written to 'bbc_trending_headlines.txt'")
