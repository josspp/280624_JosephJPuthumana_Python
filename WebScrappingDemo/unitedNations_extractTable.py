import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL for the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"

# Send the HTTP request and get the response
response = requests.get(url)

# Parse the response with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find the table with the class 'wikitable' (this is the one we want)
table = soup.find("table", {"class": "wikitable"})

# Extract the table headings (headers) from the first row (<th>)
headers = [header.text.strip() for header in table.find_all("th")]

# Initialize a list to store the rows of the table
data = []

# Loop through the rows of the table (excluding the header row)
for row in table.find_all("tr")[1:]:
    columns = row.find_all("td")
    if len(columns) >= len(headers):  # Only process rows with at least the same number of columns as headers
        # Extract each cell in the row
        row_data = [column.text.strip() for column in columns]
        
        # Add the row to the data list
        data.append(row_data)

# Create a DataFrame from the list of data and the headers
df = pd.DataFrame(data, columns=headers)

# Write the DataFrame to a CSV file
df.to_csv("countries_by_population_full.csv", index=False)

print("Table data with all columns has been written to 'countries_by_population_full.csv'")
