def calc_VAT(inputPrice, option, rate):
    newPrice = 0
    if option == "add":
        newPrice = inputPrice * (rate/100 + 1)
    elif option == "remove":
        newPrice = inputPrice / (rate/100 + 1)
    return newPrice

salestotal = 139
option = "add"
market = "UK"
if market == "UK" or market == "FR":
    rate = 20
elif market == "DE":
    rate = 19
finalprice = calc_VAT(salestotal, option, rate)
print("The price with VAT is ", finalprice)
