import requests
import datetime
import json
#eaefa97c91482882ff25d3e58d0b9ca7 api key


url="https://api.exchangerate.host/live?access_key=eaefa97c91482882ff25d3e58d0b9ca7"

params ={"base":"USD"}

response = requests.get(url,params)

print(response.json())

if(response.status_code==200):
    rates=response.json()["quotes"]
    filename= "exchange_rates_{val}.json".format(val = datetime.date.today())

    with open(filename,'w') as file:
        json.dump(rates,file)


print("data dumped in the file")

