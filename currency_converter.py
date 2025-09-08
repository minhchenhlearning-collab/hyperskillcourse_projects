# write your code here!
conicoins = float(input("Please, enter the number of conicoins you have:"))
currency_value = {"RUB":2.98, "ARS":0.82, "HNL":0.17, "AUD":1.9622, "MAD":0.208}
for currency, value in currency_value.items():
    print(f"I will get {value} {currency} from the sale of {conicoins} conicoins.")