import requests
from bs4 import BeautifulSoup
import pandas as pd

url= "https://www.worldometers.info/world-population/"
response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')
#print(soup)

# Get the text of class
i = 0
master_list=[]
col_names = ""

table_data = soup.find('table')
rows_data = table_data.find_all('tr')
for colname in table_data.find_all('th'):
    col_names += colname.text


for row in rows_data:
    cells = row.find_all('td')
    data = [cell.text.strip() for cell in cells]
    print(rows_data)
    #print(type(data))
    master_list.append(data)
    
df = pd.DataFrame(master_list)
print(col_names)
print(df)