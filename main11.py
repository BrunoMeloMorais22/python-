
try:
    print(x)

except NameError:
    print('Variable X is not defined')

except:
    print('Something else went wrong')