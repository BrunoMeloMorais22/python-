import pandas as pd

itens = {
    "NameItem" : ["Colher", "Mouse", "Estojo", "Pulseira"],
    "PriceItem" : [29.99, 30.99, 12.99, 'arroz']
}

x = pd.DataFrame(itens, index = ["day1", "day2", "day3", "day4"])
x.loc["day4", "PriceItem"] = 9.99

print(x.tail(2))