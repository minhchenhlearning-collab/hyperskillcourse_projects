import requests

currency = input().lower()
url = f"https://www.floatrates.com/daily/{currency}.json"   
try:    
    r = requests.get(url).json()
    usd_rate = r["usd"]
    eur_rate = r["eur"]
    print(usd_rate, eur_rate, sep="\n")
except requests.exceptions.ConnectionError:
    print("Connection Failed")
