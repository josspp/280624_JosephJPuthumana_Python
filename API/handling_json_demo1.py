import requests

url="https://api.coingecko.com/api/v3/simple/price"
params={
    "ids":"bitcoin,ethereum","vs_currencies":"inr"
}

reponse = requests.get(url,params)

print(reponse.json())

data=reponse.json()

bitcoin_price_in_inr = data["ethereum"]["inr"]

print(bitcoin_price_in_inr)




