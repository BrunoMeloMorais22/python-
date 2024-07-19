

try:
    number = int(input('Digite um número por favor: '))
    print(number)
except ValueError:
    print('Você não digitou um número.')

else:
    print(f'O usuário digitou o número {number}')