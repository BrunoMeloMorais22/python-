import pandas as pd

myproducts = {
    "NameProducts" : ["Mouse", "Guarda Roupa", "Mesa", "Chuveiro", "Torneira", "Cobertor", "Ventilador de Chão"],
    "Price" : [79.99, 249.99, 149.99, 99.99, 69.99, 29.99, 'reais']
}

x = pd.DataFrame(myproducts, index = ["day1", "day2", "day3", "day4", "day5", "day6", "day7"])
x.loc["day7", "Price"] = 39.99

print(x)