import pandas as pd

a = [1, 2, 3]

x = pd.Series(a, index = ["x", "y", "z"])



print(x["z"])