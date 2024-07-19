import pandas as pd

books = {
    "Books" : ["O pequeno príncipe", "O diário de Anne Frank", "Hackers", "Submundo"],
    "Price" : [15, 20, 'arroz' , 30]
}

x = pd.DataFrame(books)
x.loc[2, "Price"] = 25

print(x)