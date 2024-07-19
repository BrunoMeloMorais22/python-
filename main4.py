
cor_cliente = input('Digite a cor desejada por favor: ')

colors = ['amarela', 'lilás', 'verde', 'azul', 'preto', 'vermelha', 'roxo', 'rosa']

if cor_cliente.lower() in colors:
    print('Cor disponível.')

else:
    print('Cor não disponível.')