import pandas as pd

fruits = {
    "NameFruits" : ["Banana", "Maça", "Abacate", "Abacaxi"],
    "PriceFruits" : [8.99, 12.30, 19.99, 'arroz']
}

x = pd.DataFrame(fruits, index = ["day1", "day2", "da3", "day4"])
x.loc["day4", "PriceFruits"] = 21.99
print(x)