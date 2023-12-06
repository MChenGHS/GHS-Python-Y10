def calculate(salestotal, rate):
    finalprice = salestotal * (1 + rate / 100)
    return finalprice

def market_to_rate(market):
    if market == "UK" or market == "FR":
        rate = 20
    elif market == "DE":
        rate = 19
    return rate

# Product 1
salestotal = 100
option = "add"
market = "UK"
rate = market_to_rate(market)

finalprice = calculate(salestotal, rate)
print("The price with VAT is ", finalprice)

# Product 2
salestotal = 50
option = "add"
market = "DE"
rate = market_to_rate(market)

finalprice = calculate(salestotal, rate)
print("The price with VAT is ", finalprice)