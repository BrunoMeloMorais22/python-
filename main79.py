
import pandas as pd

myproducts = {
    "NameProduct" : ["Mouse", "Keyboard", "Notebook", "Closet"],
    "PriceProduct" : [139.99, 4934343 ,2599.99, 1999.99]
}

x = pd.DataFrame(myproducts, index = ["day1", "day2", "day3", "day4"])
x.loc["day2", "PriceProduct"] = 899.99
print(x)