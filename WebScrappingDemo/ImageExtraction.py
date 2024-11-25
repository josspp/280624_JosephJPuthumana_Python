import requests
from bs4 import BeautifulSoup
import pandas as pd

url= "https://unsplash.com/s/photos/nature"
response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')

images = soup.find_all('img',{"srcset":True})
image_url=images[-1]
image_url=image_url['src']
print(image_url)

img_data = requests.get(image_url).content
image_path = "sample_image.jpg"

with open(image_path,"wb") as img_file_handler:
    img_file_handler.write(img_data)

#image_data = []


for img in images:
    image_url=img['src']
    img_data = requests.get(image_url).content
    image_path = f"./Images/{img['alt']}.jpg"

    with open(image_path,"wb") as img_file_handler:
        img_file_handler.write(img_data)

#df = pd.DataFrame(image_data)
#print(df)
#df.to_csv("ImageData.csv")
