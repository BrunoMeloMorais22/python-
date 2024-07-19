import pandas as pd

people = {
    "Name" : ['Marcelo', 'Gustavo', 'Breno'],
    "idade" : [19, 20, 22]
}

x = pd.DataFrame(people)

print(x)