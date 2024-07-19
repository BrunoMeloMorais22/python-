products = ['juice', 'chocolate', 'water']
user_choise = 2

try:
    print(products[user_choise])

except IndexError:
    print('O index não existe')

except:
    print(products[user_choise])