import requests
from bs4 import BeautifulSoup

url= "https://example.com/"
response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')
#print(soup)

h1_tag = soup.find('h1')
if(h1_tag):
    print("Found the H1 tag and the text inside it is : ")
    print(h1_tag.text)

links_tags = soup.find_all('a')
for link in links_tags:
    href = link.get('href')    
    print(href)

p_tags = soup.find_all('p')
for para in p_tags:
    para_text = para.text
    print(f'\n\n--------------------------------New paragraph---------------------------------')    
    print(para_text)    
    print('--------------------------------Paragraph ends--------------------------------') 