import requests
import pandas as pd

url="https://jsonplaceholder.typicode.com/users"


response= requests.get(url)

if(response.status_code==200):
    print("everything is fine")
    #print(response.json())

else:
    print("Some issue happened", str(response.status_code))



df=pd.DataFrame(response.json())
print(df)