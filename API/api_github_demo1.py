
import requests
import pandas as pd

url="https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=2"


response= requests.get(url)
#print(response.json())
if(response.status_code==200):
    print("everything is fine")
    print(response.json())

else:
    print("Some issue happened", str(response.status_code))



#df=pd.DataFrame(response.json())
#print(df)