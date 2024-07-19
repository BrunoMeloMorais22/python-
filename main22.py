
try:
    valor = int(input('Digite o valor do seu produto por favor: '))
    print(valor)

except ValueError:
    print('Por favor digitar apenas números.')

else:
    print('O usuário digitou o valor do seu produtor')
    print(valor * 2)

