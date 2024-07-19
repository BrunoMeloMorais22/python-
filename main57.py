
try:
    numbers = [1, 2, 3, 4]
    print(numbers[5])

except IndexError:
    print('O index solicitado não existe.')
    print('Tente outro index.')

else:
    print(f'Tudo ocorreu bem')