import pandas as pd


mylist = {
    "name" : ['Arroz', 'Feijão', 'Batata'],
    "price" : [29.99, 44,99, 12.99]
}

df = pd.DataFrame(mylist)

print(df)