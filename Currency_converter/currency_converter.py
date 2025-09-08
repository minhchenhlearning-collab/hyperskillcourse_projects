import requests

def default_cache(currency):
    global cache
    cache = {}
    url = f"https://www.floatrates.com/daily/{currency}.json"   
    try:
        global r    
        r = requests.get(url).json()
        if currency != "usd":
            cache["usd"] = r["usd"]["rate"]
        if currency != "EUR":
            cache["eur"] = r["eur"]["rate"]
    except requests.exceptions.ConnectionError:
        print("Connection Failed")
def converting(currency, convert_to, amount):
    print("Cheking in the cache...")
    if convert_to in list(cache.keys()):
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cache[convert_to] = r[convert_to]["rate"]
    converted = round(amount*cache[convert_to], 2)
    print(f"You received {converted} {convert_to.upper()}.")

currency = input().lower()
while True:
    convert_to = input().lower()
    if convert_to == "":
        break
    amount = float(input())
    default_cache(currency)
    converting(currency, convert_to, amount)
